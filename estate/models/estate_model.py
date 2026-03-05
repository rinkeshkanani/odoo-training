from odoo import models,api,fields

class RealEstate(models.Model):
    _name = 'real.estate'
    _description = 'Real Estate'

    name = fields.Char(string="Name",required=True)
    description = fields.Text(string="description")
    postcode = fields.Char(string='postcode')
    date_availability = fields.Date(string="date_avilability")
    expected_price = fields.Float(string="expected_price",required=True)
    selling_price = fields.Float(string="selling_price")
    bedrooms = fields.Integer(string="bedrooms")
    living_area = fields.Integer(string="living_area")
    facades = fields.Integer(string="facades")
    garage = fields.Boolean(string="garage",default=False)
    garden = fields.Boolean(string="garden")
    garden_area = fields.Integer(string="garden")
    garden_orientation = fields.Selection([('north','North'),('south','South'),('east','East'),('west','West')])
