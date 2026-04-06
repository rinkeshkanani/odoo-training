from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime,timedelta
class SaleOrderCustom(models.Model):
    _inherit = "sale.order"

    note_any = fields.Text(string="Note")
    customer_phone = fields.Char(string="Customer Phone",null=False)
    risk_level = fields.Selection([('high','High'),('medium','Medium'),('low','Low')],string="Risk Level",tracking=True)
    def _prepare_invoice(self):
        res = super()._prepare_invoice()
        res['note_any'] = self.note_any
        res['customer_phone'] = self.customer_phone
        return res

    @api.constrains('customer_phone')
    def _check_phone(self):
        if self.customer_phone:
            if len(self.customer_phone) != 10:
                raise ValidationError("The phone number must be 10 digits!!!")

    _phone_check = models.Constraint(
        'UNIQUE(customer_phone)','The Phone Number Should be unique!!',
    )

    def action_open_wizard(self):
        self.ensure_one()
        return ({
            'type': 'ir.actions.act_window',
            'name': 'manage sale order',
            'res_model': 'sale.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                 'active_id': self.id,
            }
        }
        )



# task1 sale order confirm by 6 pm
    @api.model
    def sale_schedule(self):
        records = self.search([('state','=','draft')])
        for rec in records:
            rec.action_confirm()

#  task2 :Automatically cancel quotations that are older than 7 days and not confirmed.
    @api.model
    def sale_quotation_schedule(self):
        before_today = datetime.today() - timedelta(days=7)
        records = self.search([('state','=','draft')])
        for rec in records:
            if rec.date_order <= before_today:
                rec.action_cancel()

# task 3: Server action risk level
    def risk_level_server(self):
        for rec in self:
            if rec.amount_total:
                if rec.amount_total >50000:
                    rec.risk_level = 'high'
                elif 10000 < rec.amount_total <= 50000:
                    rec.risk_level = 'medium'
                else:
                    rec.risk_level = 'low'

# task email on confirm sell order
    def action_confirm(self):

        template = self.env.ref('sale_order_wizard.email_confirm_sale_order')
        for rec in self:
            email_values={
                'email_to': rec.partner_id.email,
            }
            template.send_mail(rec.id,force_send=True,email_values=email_values)
        return super().action_confirm()



class SaleOrderLineCustom(models.Model):
    _inherit = "sale.order.line"

    @api.constrains('product_uom_qty')
    def _check_product_uom_qty(self):
        for rec in self:
            if rec.product_uom_qty and rec.product_uom_qty > 50:
                raise ValidationError("The product quantity must be less than 50!!!")

