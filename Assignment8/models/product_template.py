from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_book_product = fields.Boolean("Created From Book")
    book_id = fields.Many2one("library.book", string="Book")

    book_count = fields.Integer(compute="_compute_book_count")

    def _compute_book_count(self):
        for rec in self:
            rec.book_count = 1 if rec.book_id else 0

    def action_view_book(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'library.book',
            'view_mode': 'form',
            'res_id': self.book_id.id,
        }
