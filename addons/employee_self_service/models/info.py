from odoo import models, fields

class InfoUpdateRequest(models.Model):
    _name = 'info.update.request'
    _description = 'Employee Information Update Request'
    _rec_name = 'employee_id'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    field_to_update = fields.Char(string='Field to Update')
    old_value = fields.Char(string='Old Value')
    new_value = fields.Char(string='New Value')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft')
