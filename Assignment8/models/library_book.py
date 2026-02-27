from odoo import models, fields, api
from odoo.exceptions import UserError


class LibraryBook(models.Model):
    _inherit = "library.book"

    product_ids = fields.One2many(
        "product.template",
        "book_id",
        string="Products"
    )

    product_count = fields.Integer(
        compute="_compute_product_count"
    )

    def _compute_product_count(self):
        for rec in self:
            rec.product_count = len(rec.product_ids)

    # ============================================================
    # CREATE PRODUCT BUTTON
    # ============================================================

    def action_create_product(self):
        self.ensure_one()

        if not self.book_edition_ids:
            raise UserError("Please add at least one Edition.")

        attribute = self.env.ref(
            'ak_library_management_orm.attribute_editions'
        )

        # --------------------------------------------------
        # 1️⃣ CATEGORY CREATE / FIND
        # --------------------------------------------------
        product_category = self._get_or_create_product_category()

        # --------------------------------------------------
        # 2️⃣ CREATE ATTRIBUTE VALUES FROM EDITIONS
        # --------------------------------------------------
        attribute_values = []

        for edition in self.book_edition_ids:

            value = self.env['product.attribute.value'].search([
                ('name', '=', edition.name),
                ('attribute_id', '=', attribute.id)
            ], limit=1)

            if not value:
                value = self.env['product.attribute.value'].create({
                    'name': edition.name,
                    'attribute_id': attribute.id,
                })

            attribute_values.append(value.id)

        # --------------------------------------------------
        # 3️⃣ CREATE PRODUCT TEMPLATE
        # --------------------------------------------------
        product = self.env['product.template'].create({
            'name': self.name,
            'type': 'consu',
            'is_storable': True,
            'is_book_product': True,
            'book_id': self.id,
            'categ_id': product_category.id,
            'attribute_line_ids': [(0, 0, {
                'attribute_id': attribute.id,
                'value_ids': [(6, 0, attribute_values)]
            })]
        })

        # --------------------------------------------------
        # 4️⃣ UPDATE VARIANT PRICE & STOCK
        # --------------------------------------------------
        self._update_variant_data(product)

    # ============================================================
    # CATEGORY LOGIC
    # ============================================================

    def _get_or_create_product_category(self):

        ProductCategory = self.env['product.category']

        product_category = ProductCategory.search([
            ('book_categ_id', '=', self.category_id.id)
        ], limit=1)

        if product_category:
            return product_category

        parent_product_category = False

        if self.category_id.parent_id:
            parent_product_category = ProductCategory.search([
                ('book_categ_id', '=', self.category_id.parent_id.id)
            ], limit=1)

            if not parent_product_category:
                parent_product_category = ProductCategory.create({
                    'name': self.category_id.parent_id.name,
                    'book_categ_id': self.category_id.parent_id.id,
                })

        return ProductCategory.create({
            'name': self.category_id.name,
            'parent_id': parent_product_category.id if parent_product_category else False,
            'book_categ_id': self.category_id.id,
        })

    # ============================================================
    # UPDATE VARIANT PRICE & QUANTITY
    # ============================================================

    def _update_variant_data(self, product):

        stock_location = self.env.ref('stock.stock_location_stock')

        for edition in self.book_edition_ids:

            variant = product.product_variant_ids.filtered(
                lambda v: edition.name in v.attribute_value_ids.mapped('name')
            )

            if not variant:
                continue

            # ✅ Update Sale Price
            variant.write({
                'lst_price': edition.price
            })

            # ✅ Update On Hand Quantity
            self.env['stock.quant'].create({
                'product_id': variant.id,
                'location_id': stock_location.id,
                'quantity': edition.quantity,
            })

    # ============================================================
    # SMART BUTTON
    # ============================================================

    def action_view_products(self):
        self.ensure_one()

        if len(self.product_ids) == 1:
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'product.template',
                'view_mode': 'form',
                'res_id': self.product_ids.id,
            }

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'product.template',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.product_ids.ids)],
        }
