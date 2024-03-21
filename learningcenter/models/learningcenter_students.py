from odoo import fields, models, api
from odoo.exceptions import ValidationError



class LearningCenterStudent(models.Model):
    _name="learningcenter.student"
    _description="O'quv markazi o'quvchilari"

    name = fields.Char(string="O'quvchi FIOsi", required=True)
    phone_number = fields.Char(string="O'quvchi tel raqami", required=True)
    birthdate = fields.Date(string="O'quvchi tug'ilgan kuni")
    description = fields.Text(string='Izoh')
    group_ids = fields.Many2many('learningcenter.group', string='Guruhlar')
    payment_ids = fields.One2many('learningcenter.payment', 'student_id', string='To\'lovlar')


    @api.constrains('phone_number')
    def _check_phone_number_format(self):
        for record in self:
            number_and_length = not record.phone_number.isdigit() or len(record.phone_number) != 12
            is_uzbek_number = str(record.phone_number).startswith("998")
            if number_and_length and is_uzbek_number:
                raise ValidationError("Telefon raqami notog'ri kiritildi. 998996405599 shu ko'rinishda kiriting!")
