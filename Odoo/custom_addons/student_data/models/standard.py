from odoo import fields, models, api


class StudentStandard(models.Model):
    _name = "student.standard"
    _description = "Student Standard"

    name_id = fields.Many2one('student.data', string="Name")
    stand = fields.Integer(string="Standard")