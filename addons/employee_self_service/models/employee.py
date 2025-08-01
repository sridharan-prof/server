from odoo import fields, api, models

class EmployeeSelfService(models.Model):
    _name = "employee.selfservice"
    _description = "Employee Self-Service Details"
    _rec_name = 'name'

    reference = fields.Char(string="Reference", default = "New")
    name = fields.Many2one('hr.employee', string='employee', required=True)
    department_id = fields.Many2one('hr.department', string='Department')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == "New":
                vals['reference'] = self.env['ir.sequence'].next_by_code('employee.selfservice')
        return super().create(vals_list)