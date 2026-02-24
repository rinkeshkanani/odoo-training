from odoo import models, fields

class HrCustom(models.Model):
    _inherit = "hr.employee"
    notes = fields.Char(string="Notes")

class EmployeeActionWizard(models.TransientModel):
    _name = "employee.action.wizard"
    _description = "Employee Action Wizard"

    employee_action = fields.Char(string="Employee Action")

    def create_action_wizard(self):
        print("create_action_wizard")
