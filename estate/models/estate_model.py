from odoo import models,api,fields

class RealEstate(models.Model):
    _name = 'real.estate'
    _description = 'Real Estate'

    name = fields.Char(string="Name",required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string="Date Availability",copy=False)
    expected_price = fields.Float(string="Expected Price",required=True,default=1)
    selling_price = fields.Float(string="Selling Price",copy=False)
    price = fields.Float(string="Price")
    bedrooms = fields.Integer(string="Bedrooms",default=2)
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection([('north','North'),('south','South'),('east','East'),('west','West')])
    active = fields.Boolean(string="Active",default=True)
    state = fields.Selection([('new','New'),('offer_received','Offer Received'),('sold','Sold'),('cancelled','Cancelled')],string="State",default='new')


    #external id
    property_type_id = fields.Many2one('estate.property.type',string="Property Type")
    tag_ids = fields.Many2many('estate.property.tag',string="Tags")
    property_id = fields.One2many('estate.property.offer','property_ids',string='Property Types')
    salesperson_id = fields.Many2one('res.users',string="Salesperson",default= lambda self: self.env.user.id)
    buyer_id = fields.Many2one('res.partner',string="Buyer",copy=False)