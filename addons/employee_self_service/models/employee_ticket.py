from odoo import fields, models, api

class employee_ticket(models.Model):
    _name = "employee.ticket"
    _inherit = ['mail.thread']
    _description = "employee ticket"

    name = fields.Char(string='Subject')
    employee_id = fields.Many2one('hr.employee', string='Employee', default=lambda self: self.env.user.employee_id)
    department_id = fields.Many2one('hr.employee', string='Department')
    category = fields.Selection([('hr', 'HR'), ('it', 'IT'), ('payroll', 'Payroll')], string='Category')
    description = fields.Text(string='Description')
    attachment = fields.Binary(string='Attachment')
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('resolved', 'Resolved')], default='draft')

    @api.model
    def create(self, vals):
        record = super().create(vals)
        template = self.env.ref('employee_self_service.employee_ticket_email_template')
        if template:
            template.send_mail(record.id, force_send=True)
        return record