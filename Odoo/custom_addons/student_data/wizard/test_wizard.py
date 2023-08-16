from odoo import api, fields, models


class TestWizard(models.TransientModel):
    _name = "test.wizard"
    _description = "Test Wizard"

    name = fields.Char(string="Name")
    subject_ids = fields.Many2many('student.subject', string="Subject")

    def action_create(self):
        student_id = self.env[self._context['active_model']].browse(self._context['active_ids'])
        student_id.subject_ids = [(0, 0, {'subject': self.name})]
        print("............for create",student_id.subject_ids)

    def action_update(self):
        student_id = self.env[self._context['active_model']].browse(self._context['active_ids'])
        # print("subject ki id",self.subject_ids.id)
        # print("name ki id",self.name.id)
        student_id.subject_ids = [(1, self.subject_ids.id, {'subject': self.name})]
        # print("............for update", student_id.subject_ids)
    #
    #
    # def action_delete(self):
    #     student_id = self.env[self._context['active_model']].browse(self._context['active_ids'])
    #     student_id.subject_ids = [(2, self.subject_ids.id)]
    #     print("delete working")
    #
    # def action_remove(self):
    #     student_id = self.env[self._context['active_model']].browse(self._context['active_ids'])
    #     student_id.subject_ids = [(3, self.subject_ids.id)]
    #     print("remove worked")
    #
    # def action_name_change(self):
    #     student_id = self.env[self._context['active_model']].browse(self._context['active_ids'])
    #     student_id.subject_ids = [(4, self.subject_ids.id)]
    #     print("Name Changed")
    #
    # def action_unlink_all(self):                            # worked
    #     student_id = self.env[self._context['active_model']].browse(self._context['active_ids'])
    #     student_id.subject_ids = [(5, self.subject_ids.id)]
    #     print("Unlinked all")
    #
    # def action_replace(self):
    #     student_id = self.env[self._context['active_model']].browse(self._context['active_ids'])
    #     student_id.subject_ids = [(6, 0, self.subject_ids.id)]
    #     print("Replace All")
