from odoo import fields, models, api
from odoo.exceptions import UserError

class Attendance(models.Model):
    _name = 'employee.attendance'
    _description = "Employee Attendance"
    _rec_name = "employee_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    employee_id = fields.Many2one('hr.employee', required=True)
    date = fields.Date(string="Date", compute='_compute_date', store=True)
    check_in = fields.Datetime(string="Check In", required=True)
    check_out = fields.Datetime(string="Check Out")
    duration = fields.Float(string="Duration (Hours)", compute='_compute_duration', store=True)

    @api.depends('check_in', 'check_out')
    def _compute_duration(self):
        for rec in self:
            if rec.check_in and rec.check_out:
                hours = (rec.check_out - rec.check_in).total_seconds() / 3600.0
                if hours > 10:
                    raise UserError("Single session can't exceed 10 hours.")
                rec.duration = hours

    @api.depends('check_in')
    def _compute_date(self):
        for rec in self:
            rec.date = rec.check_in.date() if rec.check_in else False

    @api.constrains('check_in', 'check_out')
    def _check_time_order(self):
        for rec in self:
            if rec.check_in and rec.check_out and rec.check_out <= rec.check_in:
                raise UserError("Check-out must be after check-in.")

    @api.constrains('check_in', 'check_out', 'employee_id')
    def _check_overlap(self):
        for rec in self:
            overlapping = self.search([
                ('id', '!=', rec.id),
                ('employee_id', '=', rec.employee_id.id),
                ('check_in', '<=', rec.check_out),
                ('check_out', '>=', rec.check_in),
            ])
            if overlapping:
                raise UserError("Overlapping attendance records are not allowed.")
