from odoo import fields, models, api

class EmployeePayslip(models.Model):
    _name = "employee.payslip"
    _description = "Employee Payslip"
    _rec_name = 'employee_id'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    paymonth_slip = fields.Date(string="Payslip Date", required=True)
    gross_salary = fields.Float(string='Gross Salary', required=True)
    deduction = fields.Float(string='Deductions', required=True)
    net_salary = fields.Float(string='Net Salary', compute='compute_net_salary', store=True)

    @api.depends('gross_salary', 'deduction')
    def compute_net_salary(self):
        for rec in self:
            rec.net_salary = rec.gross_salary - rec.deduction
