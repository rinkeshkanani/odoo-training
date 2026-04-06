from odoo import models, fields

class HrCustom(models.Model):
    _inherit = "hr.employee"
    notes = fields.Char(string="Notes")
    employee_ids = fields.One2many('employee.query','employee_id',string="Employees")

    def create_query(self):
        return{
            'type': 'ir.actions.act_window',
            'name': 'Employee Query',
            'res_model': 'employee.query',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_employee_action': 'Test'
            }
        }

class EmployeeActionWizard(models.TransientModel):
    _name = "employee.action.wizard"
    _description = "Employee Action Wizard"

    employee_action = fields.Char(string="Employee Action")

    def create_action_wizard(self):
        print("create_action_wizard")


class EmployeeQueries(models.Model):
    _name = "employee.query"
    _description = "Employee Queries"

    employee_id = fields.Many2one('hr.employee',string="Employee")
    employee_query_type = fields.Selection([('device','Device'),('culture','Culture'),('other','Other')],default='other',string="Employee Query Type")
    employee_query = fields.Char(string="Employee Query")





