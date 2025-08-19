from odoo import fields, models

class EmployeeTag(models.Model):
    _name = "employee.tag"
    _description = "Employee Tag"

    name = fields.Char(string = "Skill")
    