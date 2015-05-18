# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval

__all__ = ['ShipmentOut', 'ShipmentIn']
__metaclass__ = PoolMeta


class ShipmentOut:
    __name__ = 'stock.shipment.out'
    review = fields.Boolean('Review')
    review_description = fields.Text('Review Description',
        states={
            'invisible': ~Eval('review'),
            },
        depends=['review'],
        )

    @classmethod
    def done(cls, shipments):
        super(ShipmentOut, cls).done(shipments)
        cls.write(shipments, {'review': False})


class ShipmentIn:
    __name__ = 'stock.shipment.in'

    @classmethod
    def _get_inventory_moves(cls, incoming_move):
        pool = Pool()
        ModelData = pool.get('ir.model.data')
        ProductReviewType = pool.get('product.review.type')
        ConfigurationLocation = pool.get('stock.configuration.location')

        move = super(ShipmentIn, cls)._get_inventory_moves(incoming_move)

        product = move.product.template
        if product.review:
            review_type = ProductReviewType(
                ModelData.get_id('stock_shipment_review',
                    'product_review_type_review_location'))
            if review_type in product.review_types:
                location = move.to_location
                while location.parent and location.type != 'warehouse':
                    location = location.parent
                review_locations = ConfigurationLocation.search([
                        ('warehouse', '=', location)
                        ])
                if review_locations:
                    move.to_location = review_locations[0].location
        return move
