{
    'name': "Sales Management",
    'version': "1.0",
    'depends': ['base', 'web', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/inventory_views.xml',
        'views/sales_order_views.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sales_management/static/src/css/dashboard.css',
            'sales_management/static/src/js/sales_dashboard.js',
            'sales_management/static/src/xml/sales_dashboard.xml',
        ],
    },
    'application': True,
}
