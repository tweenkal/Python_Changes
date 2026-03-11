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

    def _compute_product_count(self):
        for rec in self:
            rec.product_count = len(rec.product_ids)

    def action_create_product(self):

        ProductTemplate = self.env['product.template']
        ProductCategory = self.env['product.category']
        Attribute = self.env.ref(
            'ak_library_product_extension.attribute_book_edition'
        )

        for book in self:

            # find or create category
            categ = ProductCategory.search([
                ('book_categ_id', '=', book.category_id.id)
            ], limit=1)

            if not categ:
                categ = ProductCategory.create({
                    'name': book.category_id.name,
                    'book_categ_id': book.category_id.id
                })

            # create attribute values
            values = []
            for edition in book.edition_ids:
                val = self.env['product.attribute.value'].search([
                    ('name', '=', edition.name),
                    ('attribute_id', '=', Attribute.id)
                ], limit=1)

                if not val:
                    val = self.env['product.attribute.value'].create({
                        'name': edition.name,
                        'attribute_id': Attribute.id
                    })

                values.append(val.id)

            attribute_line = [(0, 0, {
                'attribute_id': Attribute.id,
                'value_ids': [(6, 0, values)]
            })]

            product = ProductTemplate.create({
                'name': book.name,
                'type': 'consu',
                'is_storable': True,
                'is_book_product': True,
                'book_id': book.id,
                'categ_id': categ.id,
                'attribute_line_ids': attribute_line
            })

            # update variant price and quantity
            for variant in product.product_variant_ids:

                for edition in book.edition_ids:

                    if edition.name in variant.display_name:

                        variant.lst_price = edition.price

                        self.env['stock.quant'].create({
                            'product_id': variant.id,
                            'location_id': self.env.ref('stock.stock_location_stock').id,
                            'quantity': edition.quantity
                        })

    def action_view_products(self):

        products = self.product_ids

        if len(products) == 1:
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'product.template',
                'view_mode': 'form',
                'res_id': products.id
            }

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'product.template',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', products.ids)]
        }
