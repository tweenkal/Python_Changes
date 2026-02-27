from odoo import models, fields


class ProductCategory(models.Model):
    _inherit = "product.category"

    book_categ_id = fields.Many2one(
        "book.category",
        string="Book Category"
    )

    def action_view_book_category(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'book.category',
            'view_mode': 'form',
            'res_id': self.book_categ_id.id,
        }
