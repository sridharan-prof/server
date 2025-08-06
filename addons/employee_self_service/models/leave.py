from odoo import models, fields

class LeaveRequest(models.Model):
    _name = 'leave.request'
    _description = 'Leave Request'
    _rec_name = 'employee_id'

    employee_id = fields.Many2one('employee.selfservice', string='Employee')
    leave_type = fields.Selection([
        ('sick', 'Sick Leave'),
        ('casual', 'Casual Leave'),
        ('earned', 'Earned Leave'),
        ('unpaid', 'Unpaid Leave'),
    ], string='Leave Type', default='sick')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    reason = fields.Text(string='Reason')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft')

    def approve_action(self):
        self.write({'state': 'approved'})

    def rejected_action(self):
        self.write({'state': 'rejected'})
