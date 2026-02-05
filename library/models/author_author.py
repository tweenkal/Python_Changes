from odoo import models, fields

class Author(models.Model):
    _name = 'author.author'
    _description = 'Author'

    name = fields.Char(string="Author Name", required=True)
    dob_date = fields.Date(string="Date of Birth")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string="Gender")
    nationality = fields.Char()
    email = fields.Char()
    phone = fields.Char()
    social_profile = fields.Char()

    book_ids = fields.One2many(
        'author.book',
        'book_id',
        string="Books"
    )
