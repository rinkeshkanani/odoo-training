from odoo import api,models,fields


class BorrowModel(models.Model):
    _name = 'library.borrow'
    _description = 'Library borrow'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Name')
    member_id = fields.Many2one('library.member',string='Member')
    book_id = fields.Many2one('library.book',string='Book')
    borrow_date = fields.Datetime(string='Borrow Date')
    return_date = fields.Datetime(string='Return Date')
    actual_return_date = fields.Datetime(string='Actual Return Date')
    state = fields.Selection([('draft','Draft'),('issued','Issued'),('returned','Returned'),('late','Late')],string='Status')
    color = fields.Integer()