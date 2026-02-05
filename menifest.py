# -*- coding: utf-8 -*-
{
    'name': 'AK Library Management',
    'version': '1.0',
    'summary': 'Manage library books and categories',
    'category': 'Management',
    'depends': ['base', 'web'],
    'author': 'Tweenkal',
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/book_category_views.xml',
        'views/library_menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
