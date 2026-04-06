from odoo import api,fields,models

class CustomInvoice(models.Model):
    _inherit = "account.move"

    note_any = fields.Text(string="Note")
    customer_phone = fields.Char(string="Customer Phone")