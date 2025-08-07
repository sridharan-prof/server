from odoo import fields, models, api

class EmployeeFeedback(models.Model):
    _name = "employee.feedback"
    _description = "Employee Feedback"
    _rec_name = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Title', required=True)
    feedback_type = fields.Selection([
        ('hr', 'HR'),
        ('tech', 'Tech'),
        ('general', 'General')
    ], string="Type", default="general")
    message = fields.Text(string='Message', required=True)
    is_anonymous = fields.Boolean(string='Submit Anonymously', default=False)
    employee_id = fields.Many2one('hr.employee', string='Submitted By')
    submitted_by_display = fields.Char(string='Submitted By', compute="_compute_submitted_by")

    def hr_action(self):
        self.write({'status': 'hr_review'})

    @api.model
    def create(self, vals):
        if vals.get('is_anonymous'):
            vals['employee_id'] = False
        elif not vals.get('employee_id') and self.env.user.employee_id:
            vals['employee_id'] = self.env.user.employee_id.id
        return super().create(vals)

    def write(self, vals):
        if vals.get('is_anonymous'):
            vals['employee_id'] = False
        return super().write(vals)
    
    @api.depends('is_anonymous', 'employee_id')
    def _compute_submitted_by(self):
        for rec in self:
            if rec.is_anonymous:
                rec.submitted_by_display = "Anonymous"
            else:
                rec.submitted_by_display = rec.employee_id.name if rec.employee_id else ''
