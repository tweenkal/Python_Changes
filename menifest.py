# -*- coding: utf-8 -*-

{
    'name': 'AK Library Management',
    'version': '19.0.1.0.0',
    'summary': 'Manage library books and categories',
    'description': """
Library Management module for Odoo.
- Create and manage books.
- Organize books by categories.
    """,
    'category': 'Management',
    'depends': ['base', 'web'],
    'author': 'Tweenkal',
    'website': 'https://www.aktivsoftware.com',
    'data': [
        'security/ir.model.access.csv',          # access rules first
        'views/library_books_views.xml',         # book views
        'views/book_categories_views.xml',       # category views
        'views/library_menus_views.xml',         # menus
    ],
    'license': 'AGPL-3',
    'installable': True,     # module can be installed
    'auto_install': False,   # module will NOT install automatically
    'application': True,     # module shows in Apps dashboard
}
