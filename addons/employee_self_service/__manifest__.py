{
    'name': 'Employee Self Service',
    'version': '1.0',
    'depends': ['base', 'mail', 'hr'],
    'author': 'Sridharan',
    'category': 'Human Resources',
    'description': 'Employee self service',
    'data': [
        'security/ir.model.access.csv',
        'views/action_view.xml',
        'views/menuitems_view.xml',
        'data/sequence.xml',
        'views/info_view.xml',
        # 'views/payslip.xml',
        'views/leave_views.xml',
        'views/attendance.xml',
        'views/employee_views.xml',
    ],

    'installable': True,
    'application': True,
}