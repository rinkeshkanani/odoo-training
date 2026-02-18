from odoo import models, fields, api


class school_management(models.Model):
    _name = 'school_management.school_management'
    _description = 'school_management.school_management'

    name = fields.Char(required = True)
    age = fields.Integer()
    email = fields.Char()
    active = fields.Boolean(default = True)

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100


