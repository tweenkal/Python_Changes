{
    'name': 'AK Library Management',
    'version': '1.0',
    'summary': 'Library Management Module',
    'description': 'Manage books and categories in a library',
    'author': 'Your Name',
    'category': 'Education',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/book_category_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
