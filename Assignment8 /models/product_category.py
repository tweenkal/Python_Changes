from odoo import models, fields

class ProductCategory(models.Model):
    _inherit = "product.category"

    book_categ_id = fields.Many2one("book.category", string="Book Category")

    def action_view_book_category(self):
        self.ensure_one()
        if self.book_category_id:
            return {
                'name': 'Book Category',
                'type': 'ir.actions.act_window',
                'res_model': 'library.category',
                'view_mode': 'form',
                'res_id': self.book_category_id.id,
            }
