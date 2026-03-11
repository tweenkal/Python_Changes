from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    approval_required = fields.Boolean(string="Approval Required", default=False)
    approval_done = fields.Boolean(string="Approval Done", default=False)

    def action_confirm(self):

        for order in self:

            low_stock_products = []

            for line in order.order_line:
                if line.product_id.qty_available < 5:
                    low_stock_products.append(line.product_id.name)

            if low_stock_products and not order.approval_done:

                order.approval_required = True

                product_list = ", ".join(low_stock_products)

                raise UserError(
                    f"Approval needed! The following books have low stock: {product_list}"
                )

        return super(SaleOrder, self).action_confirm()

    def action_manager_approve(self):

        if not self.env.user.is_manager:
            raise UserError("Only Managers can approve the order.")

        for order in self:
            order.approval_done = True
            order.approval_required = False

    def action_manager_reject(self):

        if not self.env.user.is_manager:
            raise UserError("Only Managers can reject the order.")

        for order in self:
            order.action_cancel()
