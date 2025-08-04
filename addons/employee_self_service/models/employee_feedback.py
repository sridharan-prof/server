from odoo import fields, models

class employee_feedback(models.Model):
    _name = "employee.feedback"
    _description = "employee feedback"

    name = fields.Char(string='Title')
    feedback_type = fields.Selection([('hr', 'HR'), ('tech', 'Tech'), ('general', 'General')], default = "general")
    message = fields.Text(string='Message', required=True)
    is_anonymous = fields.Boolean(string='Submit Anonymously', default=False)
    employee_id = fields.Many2one('hr.employee', string='Submitted By')

    def hr_action(self):
        for rec in self:
            rec.status = 'hr_review'