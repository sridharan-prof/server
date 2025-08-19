from odoo import api, fields, models

class HrDepartment(models.Model):
    _inherit = "hr.department"

    total_employee = fields.Integer(
        string="Total Employees",
        compute="_compute_total_employee",
        store=False
    )

    @api.depends('member_ids', 'member_ids.active', 'member_ids.department_id')
    def _compute_total_employee(self):
        for dept in self:
            dept.total_employee = len(dept.member_ids.filtered(lambda e: e.active))
