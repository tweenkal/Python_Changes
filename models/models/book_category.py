from odoo import models, fields

class BookCategory(models.Model):
    """
    Book Category Model

    This model is used to manage different categories of books
    in the Library Management system.

    Fields:
        category_name (Char): Name of the book category.
    """
    _name = 'book.category'
    _description = 'Book Category'

    category_name = fields.Char(string='Category Name', required=True)
