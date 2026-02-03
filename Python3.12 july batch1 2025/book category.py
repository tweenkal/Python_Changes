from odoo import models, fields

class BookCategory(models.Model):
    _name = 'book.category'
    _description = 'Book Category'

    category_name = fields.Char(string="Category Name", required=True)
