from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_book_product = fields.Boolean(string="Created From Book")
    book_id = fields.Many2one("library.book", string="Book")


    def action_view_books(self):
        self.ensure_one()
        # Find all books related to this product
        books = self.env['library.book'].search([('product_ids', 'in', self.id)])

        if len(books) == 1:
            # Single book → open form view
            return {
                'name': 'Book',
                'type': 'ir.actions.act_window',
                'res_model': 'library.book',
                'view_mode': 'form',
                'res_id': books.id,
            }

        # Multiple books → open list + form view
        return {
            'name': 'Books',
            'type': 'ir.actions.act_window',
            'res_model': 'library.book',
            'view_mode': 'tree,form',
            'res_ids': books.ids,
        }
