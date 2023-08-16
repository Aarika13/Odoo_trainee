from odoo import fields, models, api, _
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError
from werkzeug import urls


class StudentData(models.Model):
    _name = "student.data"
    _description = "Student Data"
    _order = "total desc"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age", compute="_compute_age", search="_search_age", store=True)
    birth_date = fields.Date(string="Date of Birth")
    description = fields.Text(string="Description")
    state = fields.Selection([
        ('pass', 'Pass'),
        ('fail', 'Fail')], string="Status", default="pass", store=True)
    marks1 = fields.Float(string="Marks 1")
    marks2 = fields.Float(string="Marks 2")
    marks3 = fields.Float(string="Marks 3")
    total = fields.Float(string="Total", compute='_compute_total', inverse='_inverse_total', store=True)
    image = fields.Image(string="Image")
    progress = fields.Float(string="Progress", compute='_compute_progress')
    extra_details = fields.Char(string="Other Details")
    information = fields.Char(string="Information")
    details_ids = fields.Many2many('student.personal', string="Details")
    teacher_id = fields.Many2one('res.users', string="Teacher")
    subject_ids = fields.Many2many('student.subject', string="Subject")
    is_birthday = fields.Boolean(string="Birthday ?", compute="_compute_is_birthday")

    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.birth_date:
                rec.age = today.year - rec.birth_date.year
            else:
                rec.age = 0

    def _search_age(self, operator, value):
        birth_date = date.today() - relativedelta.relativedelta(years=value)
        print("birth date", birth_date)
        start_year = birth_date.replace(day=1, month=1)
        end_year = birth_date.replace(day=31, month=12)
        return [('birth_date', '>=', start_year), ('birth_date', '<=', end_year)]

    @api.depends('birth_date')
    def _compute_is_birthday(self):
        for rec in self:
            is_birthday = False
            if rec.birth_date:
                today = date.today()
                if today.day == rec.birth_date.day and today.month == rec.birth_date.month:
                    is_birthday = True
            rec.is_birthday = is_birthday

    @api.depends('total')
    def _compute_progress(self):
        for rec in self:
            rec.progress = rec.total / 3

    @api.depends('marks2')
    def _compute_total(self):
        for obj in self:
            obj.total = obj.marks1 + obj.marks2 + obj.marks3

    def _inverse_total(self):
        for obj in self:
            obj.marks2 = obj.total - (obj.marks1 + obj.marks3)

    @api.onchange('birth_date')
    def onchange_birth_date(self):
        if self.birth_date and self.birth_date.year > 2015:
            self.birth_date = None
            return {
                'warning': {
                    'title': "Age is too small:",
                    'message': "Student should be more than 8 years old. It will not be allowed.",
                }
            }

    def action_share_whatsapp(self):
        whatsapp_api_url = 'https://api.whatsapp.com/send?'
        # print()
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': whatsapp_api_url
        }

    # ORM methods
    @api.model
    def create(self, vals):
        # print(".........................",vals)
        vals.update({'name': 'student: ' + vals.get('name')})
        # print(".....AFTER.....", vals)
        return super().create(vals)

    def write(self, vals):
        # print('......BEFORE: ', self.name)
        vals['description'] = self.name
        # print("..........AFTER:", vals['name'])
        return super().write(vals)

    def unlink(self):
        # print(self)
        if self.state == "pass":
            raise ValidationError("You can' delete this , because student is pass.")
        return super().unlink()

    def copy(self, default=None):
        # print(self)
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = self.name + " (copy)"
        return super(StudentData, self).copy(default)

    def action_test_wizard(self):
        print("1111111111")
        return self.env['ir.actions.act_window']._for_xml_id('student_data.action_test_wizard')
        # return {
        #     'name': _('Test Wizard'),
        #     'type': 'ir.actions.act_window',
        #     'view_mode': 'form',
        #     'res_model': 'test.wizard',
        #     'target': 'new'
        # }
        # return self.env['ir.actions.act_window'].browse(self._context.get('student_data.action_test_wizard'))
        # action = self.env.context.get('active_ids',['student_data.action_test_wizard']).read()[0]
        # action = self._context.get('student_data.action_test_wizard').read()[0]
        # return action
        # return self.env[self.model_id.model].browse(self._context.get('test_wizard.view_test_wizard_form'))
        # return self._context('test_wizard.view_test_wizard_form')

    def action_pass(self):
        self.state = 'pass'

    def action_fail(self):
        self.state = 'fail'
