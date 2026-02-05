# -*- coding: utf-8 -*-
from odoo import models, fields

class LibraryBook(models.Model):
    """Model to store book-related details."""
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Book Title', required=True)
    isbn = fields.Char(string='ISBN Number')
    publication_date = fields.Date(string='Publication Date')
    price = fields.Float(string='Price')
    pages = fields.Integer(string='Number of Pages')
    description = fields.Html(string='Book Summary')
    image_1920 = fields.Image(string='Book Image')
    category_id = fields.Many2one('book.category', string='Category')
