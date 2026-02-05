# -*- coding: utf-8 -*-
from odoo import models, fields

class BookCategory(models.Model):
    """Model to store book categories."""
    _name = 'book.category'
    _description = 'Book Category'

    category_name = fields.Char(string='Category Name', required=True)
