# -*- coding: utf-8 -*-
{
    'name': 'AK Library Management',
    'version': '19.0.1.0.0',
    'summary': 'Manage Library Books and Categories',
    'description': 'Library Management module with books and categories.',
    'author': 'Your Name',
    'website': 'https://www.aktivsoftware.com',
    'category': 'Tools',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/book_category_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
