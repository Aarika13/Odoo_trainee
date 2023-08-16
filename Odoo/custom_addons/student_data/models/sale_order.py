from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    student_id = fields.Many2one('student.data',string="Student")


