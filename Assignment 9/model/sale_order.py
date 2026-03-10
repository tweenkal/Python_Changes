from odoo import models, fields
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    approval_required = fields.Boolean(string="Approval Required", default=False)
    approval_granted = fields.Boolean(string="Approval Granted", default=False)

    def action_confirm(self):

        for order in self:

            if not order.approval_granted:

                low_stock_books = []

                for line in order.order_line:
                    product = line.product_id

                    if product.type == "product" and product.qty_available < 5:
                        low_stock_books.append(
                            f"{product.name} (Stock: {product.qty_available})"
                        )

                if low_stock_books:
                    order.approval_required = True

                    book_list = "\n".join(low_stock_books)

                    raise ValidationError(
                        f"Approval needed! The following books have low stock:\n{book_list}"
                    )

        return super().action_confirm()

    def action_manager_approve(self):

        if not self.env.user.is_manager:
            raise ValidationError("Only Managers can approve this order.")

        for order in self:
            order.approval_granted = True
            order.approval_required = False

    def action_manager_reject(self):

        if not self.env.user.is_manager:
            raise ValidationError("Only Managers can reject this order.")

        return self.action_cancel()
