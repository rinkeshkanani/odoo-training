from odoo import api,models,fields

class LibraryMember(models.Model):
    _name = 'library.member'
    _description = "Library Member"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    partner_id = fields.Many2one('res.partner',string="Partner ID")
    borrow_count = fields.Integer(string="Borrow Count",compute='compute_borrow_count',store=True)
    member_ids = fields.One2many('library.borrow','member_id',string="Members")

    @api.depends('member_ids')
    def compute_borrow_count(self):
        for record in self:
            record.borrow_count = record.borrow_count + 1