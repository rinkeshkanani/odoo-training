from odoo import api, models, fields
from odoo.exceptions import ValidationError


class BorrowModel(models.Model):
    _name = 'library.borrow'
    _description = 'Library borrow'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Sequence', copy=False, default='New', readonly=True, required=True)
    member_id = fields.Many2one('library.member', string='Member')
    book_id = fields.Many2one('library.book', string='Book')
    borrow_date = fields.Datetime(string='Borrow Date')
    return_date = fields.Datetime(string='Return Date')
    actual_return_date = fields.Datetime(string='Actual Return Date')
    state = fields.Selection([('draft', 'Draft'), ('issued', 'Issued'), ('returned', 'Returned'), ('late', 'Late')],
                             string='Status', default="draft")
    color = fields.Integer()
    fine_amount = fields.Float(compute='compute_fine_amount', string='Fine Amount', store=True)

    # compute field for fine amount
    @api.depends('actual_return_date', 'return_date')
    def compute_fine_amount(self):
        for rec in self:
            rec.fine_amount = 0.0
            if rec.return_date and rec.actual_return_date:  # we have to check first if the data is there
                if rec.return_date < rec.actual_return_date:  # then compare it
                    rem_date = (
                                rec.actual_return_date - rec.return_date).days  # add .days as without it will not calculate
                    rec.fine_amount = rem_date * 10  # whenever different arises it will calculate eg 2*10 20 fine

    # sequence for name
    @api.model_create_multi
    def create(self, vals):  # vals is dictionary
        for rec in vals:
            code = self.env['ir.sequence'].next_by_code('library.borrow')  # first is environment then follow by model
            rec['name'] = code  # overwrite the name field with code
        res = super().create(vals)  # each time it create the record in db
        return res

    # onchange requirements
    @api.onchange("book_id")
    def change_data(self):
        for rec in self:
            if rec.book_ids.available_qty > 0:
                rec.return_date = rec.borrow_date + 7
            else:
                raise ValidationError('Out of Stocks !!')

    #action wizard to open
    def action_open_wizard(self):
        return {
            'name': 'Return Book',
            'type': 'ir.actions.act_window',
            'res_model': 'library.return.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'active_id': self.id,
                'active_model': self._name
            }
        }


class ReturnWizard(models.TransientModel):
    _name = 'library.return.wizard'
    _description = 'Library Return Wizard'

    return_date = fields.Datetime(string='Return Date')
    fine_amount = fields.Float(string='Fine Amount', readonly=True)


    # wizard action
    def action_return(self):
        active_model = self.env.context.get('active_model')
        active_id = self.env.context.get('active_id')

        record = self.env[active_model].browse(active_id)

        record.write({
            'return_date': self.return_date,
            'fine_amount': self.fine_amount,
            'state': 'returned',
            # 'available_qty': self.book_ids.available_qty - 1,

        })
        return {'type': 'ir.actions.act_window_close'}
