from odoo import fields, models, api


class StudentSubject(models.Model):
    _name = "student.subject"
    _description = "Student Subject"

    # name_id = fields.Many2one('student.data', string="Name")
    subject = fields.Char(string="Subject")
    # color = fields.Integer(string="Color")
    # maths = fields.Boolean(string="Maths")
    # science = fields.Boolean(string="Science")
    # english = fields.Boolean(string="English")
    # soc_science = fields.Boolean(string="Social Science")
    # others = fields.Char(string="Others")

