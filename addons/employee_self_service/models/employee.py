from odoo import fields, models, api
import pytz

class EmployeeSelfService(models.Model):
    _name = "employee.selfservice"
    _description = "Employee Service"
    _rec_name = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    reference = fields.Char(string="Reference", default="New", tracking=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', tracking=True)
    name = fields.Char(string="Employee Name", compute="_compute_name", store=True)
    department_id = fields.Many2one('hr.department', string='Department', tracking=True)
    skills = fields.Many2many("employee.tag")
    image = fields.Image(string="Image", max_width=200, max_height=200, attachment = False)
    job_position = fields.Char(string="Job Position", tracking=True)
    work_mobile = fields.Char(string="Work Mobile", tracking=True)
    work_mail = fields.Char(string="E-mail", tracking=True)
    work_address = fields.Char(string="Work Address", tracking=True)
    work_location = fields.Char(string="Work Location", tracking=True)
    working_hours = fields.Char(string="Working Hours", tracking=True)
    timezone = fields.Selection(selection='_tz_get', string="Time Zone", tracking=True)
    manager_id = fields.Many2one('employee.selfservice', string="Manager", tracking=True)
    child_ids = fields.One2many('employee.selfservice', 'manager_id', string="Direct Reports")

    #personal info
    #private contact
    email = fields.Char(string = "Email", tracking = True)
    phone = fields.Char(string = "Phone", tracking = True)
    language = fields.Char(string = "Language", tracking = True)

    #family status 
    martial_status = fields.Char(string = "Martial Status", tracking = True)
    
    #emergency contact
    contact_name = fields.Char(string = "Contact Name", tracking = True)
    contact_number = fields.Char(string = "Contact Number", tracking = True)

    #education level
    certificate_level = fields.Selection([("graduate", "Graduate"),("bachelor","Bachelor"),
                                          ("doctor","Doctor"),("master","Master"),("other","Other")], default = "other", tracking = True)
    field_of_study = fields.Char(string = "Field of Study", tracking = True)
    school = fields.Char(string = "School", tracking = True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("reference", "New") == "New":
                vals["reference"] = self.env['ir.sequence'].next_by_code('employee.selfservice') or 'New'
        return super().create(vals_list)

    @staticmethod
    def _tz_get():
        return [(tz, tz) for tz in pytz.all_timezones]

    def print_report(self):
        return self.env.ref('employee_self_service.action_employee_report').report_action(self)
        
    @api.depends('employee_id')
    def _compute_name(self):
        for rec in self:
            rec.name = rec.employee_id.name if rec.employee_id else "Unknown"
