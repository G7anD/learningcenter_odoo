from odoo import fields, models, api
from odoo.exceptions import ValidationError


class LearningCenterPayment(models.Model):
    _name = "learningcenter.payment"
    _description = "O'quv markazi to'lovlar"

    name = fields.Char(string="Chek haqida")
    group_id = fields.Many2one('learningcenter.group', string="Guruh", required=True)
    student_id = fields.Many2one('learningcenter.student', string="O'quvchi", required=True)
    amount = fields.Float(string="To'lov miqdori", required=True)
    payment_datetime = fields.Datetime(string="To'lov vaqti", default=fields.Datetime.now)
    chequee = fields.Binary(string="To'lov cheki", attachment=True)


    @api.constrains('amount')
    def _check_positive_amount(self):
        for record in self:
            if record.amount <= 0:
                raise ValidationError("To'lov miqdori musbat son bo'lishi kerak.")


