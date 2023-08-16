from odoo import fields, models, api
from odoo.exceptions import ValidationError


class StudentTeacher(models.Model):
    _name = "student.teacher"
    _description = "Student Teacher"
    _log_access = False

    teacher_id = fields.Many2one('res.users', string="Name", required=True)
    subject_name = fields.Char(string="Subject")

    @api.model
    def name_create(self, name):
        return self.create({'subject_name':name}).name_get()[0]