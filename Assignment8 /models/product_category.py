from odoo import models, fields

class ProductCategory(models.Model):
    _inherit = "product.category"

    book_categ_id = fields.Many2one("book.category", string="Book Category")

    def action_open_book_category(self):

    self.ensure_one()

     def action_view_book_category(self):
        self.ensure_one()
        if self.book_categ_id:
            return {
                'name': 'Book Category',
                'type': 'ir.actions.act_window',
                'res_model': 'library.book.category',
                'view_mode': 'form',
                'res_id': self.book_categ_id.id,
            }
