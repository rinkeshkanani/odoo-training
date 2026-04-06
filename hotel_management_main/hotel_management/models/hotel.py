from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HotelManagement(models.Model):
    _name = 'hotel.management'
    _description = 'Hotel Management'

    first_name = fields.Char(string = 'First Name',placeholder = 'Enter First Name',required=True)
    last_name = fields.Char(placeholder = 'Enter Last Name ',required=True)
    age = fields.Integer(string='Age',required=True)
    email = fields.Char(string = 'Email Address',required=True,index=True)
    phone = fields.Char(string = 'Phone Number',required=True)
    is_assigned = fields.Boolean(string = 'Is Assigned',default=False)


    # One2many relational with hotel.room
    room_ids = fields.One2many("hotel.room", 'customer_id', string="Room")

    # Many2many relational with hotel.management, hotel.room
    feature_ids = fields.Many2many('hotel.feature', string='Features')

    amount = fields.Float(string='Amount',required=True)
    deposit_amount = fields.Float(string='Deposit Amount',default=10000)
    amount_paid = fields.Float(string='Amount Paid',compute="compute_amount_paid",store=True)

    date_enter = fields.Datetime(string="Date Enter",default=fields.Datetime.now)
    date_exit = fields.Datetime(string="Date Exit")
    is_paid = fields.Boolean(string='Is Paid',default=False)

    @api.depends('deposit_amount','amount')
    def compute_amount_paid(self):
        for rec in self:
            rec.amount_paid = rec.amount - rec.deposit_amount
            print(rec.amount_paid)

    @api.constrains('email')
    def _check_email(self):
        for rec in self:
            if rec.email and '@' not in rec.email:
                raise ValidationError('Email Address Must Be Valid Email Address')

    _positive_age = models.Constraint(
        'CHECK(age > 18)',
        'Age must be a greater than 18.'
    )

    @api.ondelete(at_uninstall=False)
    def _check_first_name(self):
        for rec in self:
            if rec.first_name.isdigit():
                raise ValidationError('First Name should be valid.')

    # @api.model_create_multi
    # def create(self, vals_list):
    #     for rec in vals_list:
    #         if not rec.get('name'):
    #             raise ValidationError('Name cannot be empty.')
    #     return super().create(vals_list)

class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'hotel.room'

    room_type = fields.Selection([('suite','Suite'),('normal','Normal'),('luxury','Luxury')])
    room_no = fields.Char(string='Room Number',required=True)
    customer_name = fields.Char(related='customer_id.first_name',string='Customer Name',store=True)

    # Many2one relational with hotel.management
    customer_id = fields.Many2one('hotel.management', string='Customer ID')
    # Many2many relational with hotel.management, hotel.room
    feature_ids = fields.Many2many('hotel.feature', string='Features')

    @api.onchange('room_type')
    def _room_type(self):
        for rec in self:
            rec.room_type = rec.room_type or 'normal'


class HotelFeature(models.Model):
    _name = 'hotel.feature'
    _description = 'hotel.feature'
    _rec_name = 'feature_name'

    feature_name = fields.Char(string='Feature Type',required=True)
    document = fields.Reference(selection=[
        ('hotel.room','Hotel Room'),
        ('hotel.feature','Hotel Feature'),
        ('hotel.management', 'Hotel Management'),
    ],string='Hotel Feature')


