from datetime import date
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread','mail.activity.mixin']    # chatter
    _description = "Hospital Patient"

    name = fields.Char(string="Name", tracking=True)
    date_of_birth = fields.Date(string="Date of Birth")
    ref = fields.Char(string="Reference")
    age = fields.Integer(string="Age", compute='_compute_age', tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender", tracking=True, default='female')
    active = fields.Boolean(string="Active", default=True)
    appointment_id = fields.Many2one('hospital.patient',string='Appointments')
    image = fields.Image(string="Image")
    tags_ids = fields.Many2many('patient.tag', string="Tags")


    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        if self.date_of_birth > fields.Date.today():
            raise ValueError("The entered birth date is not right")
    @api.model
    def create(self, vals):                       #over-riding
        # print("Odoo mates",vals)
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        # vals['ref'] = "OMTEST"
        return super(HospitalPatient,self).create(vals)

    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient,self).write(vals)
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            # print(today)
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

    def name_get(self):
        # return [(record.id, "[%s] %s" % (record.ref,record.name)) for record in self]
        patient_list = []
        for record in self:
            # name = str(record.ref) + ' ' + str(record.name)
            # print(type(record.ref))
            patient_name = record.ref + ' ' + record.name
            patient_list.append((record.id, patient_name))
        return patient_list
        # for record in self:
        #     if self.env.get('custom_search', False):
        #         # Only goes off when the custom_search is in the context values.
        #         result.append((record.id, "{} {}".format(record.name, record.address)))
        #     else:
        #         result.append((record.id, record.name))
        # return result
