{
    'name': "Learning Center",
    'summary': """Learning Center Payment""",
    'description': """
        Learning Center Payment logging
    """,
    'license': 'LGPL-3',
    'author': "Erkin Isoyev",
    'email': "founder@quantic.uz",
    'category': 'Administration',
    'version': '0.1',
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'data/weekdays.xml',
        'data/timerange.xml',
        'views/learningcenter_course.xml',
        'views/learningcenter_groups.xml',
        'views/learningcenter_payment.xml',
        'views/learningcenter_students.xml',
        'views/learningcenter_teachers.xml',
        'views/learningcenter_actions.xml',
        'views/learningcenter_menus.xml',
    ],
}