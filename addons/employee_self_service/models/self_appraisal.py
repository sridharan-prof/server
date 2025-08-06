from odoo import fields, models

class EmployeeAppraisal(models.Model):
    _name = "employee.appraisal"
    _description = "Employee Self Appraisal"
    _rec_name = "employee_id"

    employee_id = fields.Many2one('employee.selfservice', string="Employee", required=True)
    appraisal_date = fields.Date(string='Appraisal Date', default=fields.Date.today)
    strengths = fields.Text(string='Strengths')
    improvements = fields.Text(string='Areas for Improvement')
    manager_feedback = fields.Text(string='Manager Feedback')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('reviewed', 'Reviewed'),
        ('finalized', 'Finalized'),
    ], default='draft')

    def action_review(self):
        self.write({'state': 'reviewed'})

    def action_finalize(self):
        self.write({'state': 'finalized'})
