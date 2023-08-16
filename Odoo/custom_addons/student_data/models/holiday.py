from odoo import fields, models, api


class StudentHoliday(models.Model):
    _name = "student.holiday"
    _description = "Student Holiday"

    name_holiday = fields.Char(string="Holiday")
    holiday_date = fields.Date(string="Date for Holiday")
