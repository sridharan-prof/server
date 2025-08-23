{
    'name': "Supermarket",
    'version': "1.0",
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/actions.xml',
        'views/product_views.xml',
        'views/inventory_views.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'supermarket_pos/static/src/js/pos.js',
            'supermarket_pos/static/src/xml/pos.xml',
        ],
    },
    'application': True,
    'installable' : True,
}
