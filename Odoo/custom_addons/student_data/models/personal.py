from odoo import fields, models, api
from odoo.exceptions import ValidationError


class StudentPersonal(models.Model):
    _name = "student.personal"
    _description = "Student Personal"

    student_id = fields.Many2one('student.data', string="Name", required=True)
    mobile = fields.Char(string="Mobile", tracking=True, required=True, constrains="_check_mobile")
    blood_group = fields.Selection([
        ('o_pos', 'O+'),
        ('o_neg', 'O-'),
        ('a_pos', 'A+'),
        ('b_pos', 'B+')], string="Blood Group", store=True, required=True)
    standard = fields.Integer(string="Standard", required=True)
    image = fields.Image('Image', store=True)
    email = fields.Char(string="E-mail")
    website = fields.Char(string="Website")
    # fees = fields.Monetary(string="Amount")


    @api.constrains('mobile')
    def _check_mobile(self):
        for record in self:
            if record.mobile and len(record.mobile) != 10:
                raise ValidationError("Please enter the valid number 10 digit number.")
            if not record.mobile.isdigit():
                record.mobile = None
                raise ValidationError("Please enter the valid number")
