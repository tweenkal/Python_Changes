from odoo import models, fields, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    approval_status = fields.Selection([
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string="Approval Status", default='pending')

    approval_required = fields.Boolean(string="Approval Required", default=False)

    def action_confirm(self):

        for order in self:

            # If manager approved then proceed
            if order.approval_status == 'approved':
                return super(SaleOrder, order).action_confirm()

            low_stock_books = []

            for line in order.order_line:
                if line.product_id.qty_available < 5:
                    low_stock_books.append(line.product_id.name)

            if low_stock_books:

                order.approval_required = True
                order.approval_status = 'pending'

                books = ", ".join(low_stock_books)

                raise ValidationError(
                    _("Approval needed! The following books have low stock: %s") % books
                )

        return super(SaleOrder, self).action_confirm()

    def action_approve_order(self):

        if not self.env.user.is_manager:
            raise ValidationError(_("Only managers can approve orders"))

        for order in self:
            order.approval_status = 'approved'
            order.approval_required = False

        return True

    def action_reject_order(self):

        if not self.env.user.is_manager:
            raise ValidationError(_("Only managers can reject orders"))

        for order in self:
            order.approval_status = 'rejected'

        return self.action_cancel()
