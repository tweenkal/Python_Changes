# -*- coding: utf-8 -*-
from odoo import models, fields

class BookCategory(models.Model):
    """
    Model for storing Book Categories.
    """
    _name = 'book.category'
    _description = 'Book Category'

    category_name = fields.Char(string='Category Name', required=True)
    book_ids = fields.One2many('library.book', 'category_id', string='Books')
