from odoo import fields, models, api

class payslip(models.Model):
    _name = "employee.payslip"
    _description = "Shows the employee payslip"
    _rec_name = 'employee_id'

    employee_id = fields.Many2one('hr.employee', string='employee', required = True)
    paymonth_slip = fields.Date(string = "Date", required = True)
    gross_salary = fields.Float(string = 'gross salary', required = True)
    deduction = fields.Float(string = 'deductions', required = True)
    net_salary = fields.Float(string = 'net salary', compute = 'compute_net_salary', store = True)

    @api.depends('gross_salary', 'deduction')
    def compute_net_salary(self):
        for rec in self:
            self.net_salary = rec.gross_salary - rec.deduction