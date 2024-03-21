from odoo import fields, models, api
from odoo.exceptions import ValidationError



class LearningCenterTeacher(models.Model):
    _name="learningcenter.teacher"
    _description="O'quv markazi o'qituvchilari"

    name = fields.Char(string="O'qituvchi FIOsi", required=True)
    phone_number = fields.Char(string="O'qituvchi tel raqami", required=True)
    birthdate = fields.Date(string="O'qituvchi tug'ilgan kuni")
    description = fields.Text(string='Izoh')
    group_ids = fields.One2many('learningcenter.group', 'teacher_id', string='Guruhlar')


    @api.constrains('phone_number')
    def _check_phone_number_format(self):
        for record in self:
            number_and_length = not record.phone_number.isdigit() or len(record.phone_number) != 12
            is_uzbek_number = str(record.phone_number).startswith("998")
            if number_and_length and is_uzbek_number:
                raise ValidationError("Telefon raqami notog'ri kiritildi. 998996405599 shu shablon asosida kiriting!")
