{
    'name': 'Student Manager',
    'version': '1.0',
    'depends': ['mail'],
    'author': 'Your Name',
    'category': 'Education',
    'description': 'Manage student records',
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/student_id_views.xml',
        'views/student_readonly_views.xml',
        'views/student_views.xml',

    ],
    'installable': True,
    'application': True,
}