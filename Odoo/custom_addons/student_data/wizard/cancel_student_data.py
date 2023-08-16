from odoo import api, fields, models


class CancelStudentDataWizard(models.TransientModel):
    _name = "cancel.student.data.wizard"
    _description = "Cancel Student Data Wizard"

    student_id = fields.Many2one('student.data', string="Student Name")
    reason = fields.Text(string="Reason")
    date_cancel = fields.Date(string="Cancellation Date")

    def action_cancel(self):
        print("button clicked......")
