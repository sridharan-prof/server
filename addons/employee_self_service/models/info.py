from odoo import models, fields

class InfoUpdateRequest(models.Model):
    _name = 'info.update.request'
    _description = 'Information Update Request'
    _rec_name = 'employee_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    field_to_update = fields.Char(string='Field to Update')
    old_value = fields.Char(string='Old Value')
    new_value = fields.Char(string='New Value')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft')
