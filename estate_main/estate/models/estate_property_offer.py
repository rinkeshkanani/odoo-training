from odoo import fields,models,api

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'

    price =fields.Float(string="Price")
    status = fields.Selection([('accepted','Accepted'),('refused','Refused')],string="Status")
    partner_id = fields.Many2one('res.partner',string="Customer",required=True)
    property_ids = fields.Many2one('real.estate',string="Property")