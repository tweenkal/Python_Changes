from odoo import models, fields, api


class LibraryBook(models.Model):
    _inherit = "library.book"

    product_ids = fields.One2many(
        'product.template',
        'book_id',
        string="Products"
    )

    product_count = fields.Integer(
        compute="_compute_product_count"
    )

    # ---------------------------------------------------------
    # Compute Product Count
    # ---------------------------------------------------------

    def _compute_product_count(self):
        for rec in self:
            count = 0
            for product in rec.product_ids:
                count = count + 1
            rec.product_count = count

    # ---------------------------------------------------------
    # Create Product Button
    # ---------------------------------------------------------

    def action_create_product(self):

        edition_attribute = self.env.ref(
            'ak_library_management_orm.product_attribute_editions'
        )

        for book in self:

            # -------------------------------------------------
            # Find Product Category
            # -------------------------------------------------

            category = self.env['product.category'].search(
                [('book_categ_id', '=', book.category_id.id)],
                limit=1
            )

            # -------------------------------------------------
            # Create Category if not found
            # -------------------------------------------------

            if not category:

                parent_category = False

                if book.category_id.parent_id:

                    parent_category = self.env['product.category'].search(
                        [('book_categ_id', '=', book.category_id.parent_id.id)],
                        limit=1
                    )

                    if not parent_category:
                        parent_category = self.env['product.category'].create({
                            'name': book.category_id.parent_id.name,
                            'book_categ_id': book.category_id.parent_id.id
                        })

                category = self.env['product.category'].create({
                    'name': book.category_id.name,
                    'parent_id': parent_category.id if parent_category else False,
                    'book_categ_id': book.category_id.id
                })

            # -------------------------------------------------
            # Create Attribute Values from Editions
            # -------------------------------------------------

            value_ids = []

            for edition in book.edition_ids:

                value = self.env['product.attribute.value'].search(
                    [
                        ('name', '=', edition.name),
                        ('attribute_id', '=', edition_attribute.id)
                    ],
                    limit=1
                )

                if not value:
                    value = self.env['product.attribute.value'].create({
                        'name': edition.name,
                        'attribute_id': edition_attribute.id
                    })

                value_ids.append(value.id)

            # -------------------------------------------------
            # Create Product Template
            # -------------------------------------------------

            product = self.env['product.template'].create({
                'name': book.name,
                'type': 'consu',
                'categ_id': category.id,
                'is_book_product': True,
                'book_id': book.id
            })

            # -------------------------------------------------
            # Create Attribute Line
            # -------------------------------------------------

            attribute_line = self.env['product.template.attribute.line'].create({
                'product_tmpl_id': product.id,
                'attribute_id': edition_attribute.id
            })

            attribute_line.write({
                'value_ids': value_ids
            })

            # -------------------------------------------------
            # Update Variant Price and Quantity
            # -------------------------------------------------

            for edition in book.edition_ids:

                for variant in product.product_variant_ids:

                    for attr_val in variant.product_template_attribute_value_ids:

                        if attr_val.name == edition.name:

                            variant.write({
                                'lst_price': edition.price
                            })

                            self.env['stock.quant'].create({
                                'product_id': variant.id,
                                'location_id': self.env.ref(
                                    'stock.stock_location_stock'
                                ).id,
                                'quantity': edition.quantity
                            })

    # ---------------------------------------------------------
    # Smart Button Action
    # ---------------------------------------------------------

    def action_view_product(self):
        self.ensure_one()
        products = self.product_ids  # Standard field in Odoo library module

        if len(products) == 1:
            return {
                'name': 'Product',
                'type': 'ir.actions.act_window',
                'res_model': 'product.template',
                'view_mode': 'form',
                'res_id': products.id,
            }

        return {
            'name': 'Product',
            'type': 'ir.actions.act_window',
            'res_model': 'product.template',
            'view_mode': 'tree,form',
            'res_ids': products.ids,
        }
