from odoo import models, fields, api

class StudentID(models.Model):
    _name = 'student.id'
    _inherit = ['mail.thread']
    _description = 'Student ID Creation'
    _rec_name = 'student_id'

    reference = fields.Char(string="Reference", default = "New", tracking = True)
    student_id = fields.Many2one("student.manager", string="Student", tracking = True)
    date = fields.Date(string="Date", tracking = True)
    status = fields.Selection([('draft', 'Draft'), ('submitted', 'Submitted'), ('apporved', 'Approved'), 
                               ('printed', 'Printed'), ('cancel', 'Cancel')], default = 'draft', tracking = True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == "New":
                vals['reference'] = self.env['ir.sequence'].next_by_code('student.id') # ORM
        return super().create(vals_list)
 