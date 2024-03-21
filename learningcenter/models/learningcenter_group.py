from odoo import fields, models, api


class WeekdayModel(models.Model):
    _name = "weekday.model"
    _description = "Weekdays Model"

    name = fields.Char(string="Tag Name", required=True)


class TimeRangeModel(models.Model):
    _name = "learningcenter.time.model"
    _description = "Time Range Model"

    name = fields.Char(string="Dars vaqti")


class LearningCenterGroup(models.Model):
    _name = "learningcenter.group"
    _description = "O'quv markazi guruhlari"

    course_id = fields.Many2one('learningcenter.course', string='Kurs')
    name = fields.Char(string="Guruh nomi/raqami", required=True)
    weekdays = fields.Many2many('weekday.model', string="Dars kunlari")
    start_time = fields.Many2one('learningcenter.time.model', string="Dars boshlanish vaqti")
    end_time = fields.Many2one('learningcenter.time.model', string="Darsni tugash vaqti")
    start_date = fields.Datetime(string="Kurs boshlanish vaqti")

    room = fields.Char(string="O'quv xonasi nomi/raqami")
    teacher_id = fields.Many2one('learningcenter.teacher', string='O\'qituvchi')
    student_ids = fields.Many2many('learningcenter.student', string='O\'quvchilar')
    description = fields.Text(string='Izoh')
    payment_ids = fields.One2many('learningcenter.payment', 'group_id', string='To\'lovlar')
