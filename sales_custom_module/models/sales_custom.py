from odoo import models,fields,api

class SalesCustom(models.Model):
    _inherit = 'sale.order'

    note_to_take = fields.Char(string="notes")
    internal_request = fields.Char(string="Internal Request")
    payment_method = fields.Selection([('cash','Cash'),('credit_card','Credit Card'),('upi','UPI')],default='cash')
    cust_priority = fields.Selection([('0','0'),('1 ','1'),('2','2'),('3','3'),('4','4')])
    is_paid = fields.Boolean(string="Is Paid",default=False)
    client_reaction = fields.Char(string="Client Reaction")

    amount = fields.Float(string='amount')
    to_be_paid = fields.Float(string='Total Amount',compute='_compute_to_be_paid')
    state = fields.Selection(selection_add=[('working','Working'),('not_started','Not Started')],store=True,readonly=False)
    image_field = fields.Many2many('ir.attachment')
    @api.depends('amount')
    def _compute_to_be_paid(self):
        for record in self:
            record.to_be_paid = record.amount*2.5

