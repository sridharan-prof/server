from odoo import models, fields

class Student(models.Model):
    _name = 'student.manager'
    _inherit = ['mail.thread']
    _description = 'Student Manager'

    name = fields.Char(string='Student Name', required=True, tracking = True)
    roll_number = fields.Integer(string='Roll Number', required=True)
    class_name = fields.Char(string='Class')
    email = fields.Char(string='Email')