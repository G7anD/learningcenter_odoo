from odoo import fields, models


class LearningCenterCourse(models.Model):
    _name="learningcenter.course"
    _description="O'quv markazi kurslari"

    name = fields.Char(string="Kurs nomi", required=True)
    description = fields.Text(string='Izoh')
    price  = fields.Float(string='Narxi')
    group_ids = fields.One2many('learningcenter.group', 'course_id', string='Guruhlar')
