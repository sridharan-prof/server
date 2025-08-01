from odoo import fields, models, api
from datetime import timedelta
class attendance(models.Model):
    _name = 'employee.attendance'
    _description = "employee attendance"
    _rec_name = 'employee_id'

    employee_id = fields.Many2one('hr.employee', string = 'employee')
    check_in = fields.Datetime(string = "check in")
    check_out = fields.Datetime(string = "check out")
    total_hours = fields.Float(string = "total hours",compute = 'compute_total_hour', store = True)

    @api.depends('check_in', 'check_out')
    def compute_total_hour(self):
        for record in self:
            if record.check_in and record.check_out:
                total_time = record.check_out - record.check_in
                record.total_hours = total_time.total_seconds() / 3600.0
            else:
                record.total_hours = 0.0
            