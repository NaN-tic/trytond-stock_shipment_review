# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval, Not, Bool

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

    @classmethod
    def view_attributes(cls):
        return super(ShipmentOut, cls).view_attributes() + [
            ('//page[@id="review"]', 'states', {
                    'invisible': Not(Bool(Eval('review'))),
                    })]


class ShipmentIn:
    __name__ = 'stock.shipment.in'

    @classmethod
    def _get_inventory_moves(cls, incoming_move):
        Config = Pool().get('stock.configuration')
        config = Config(1)

        move = super(ShipmentIn, cls)._get_inventory_moves(incoming_move)

        if incoming_move.product.review_location:
            for l in config.review_locations:
                if l.warehouse == incoming_move.shipment.warehouse:
                    move.to_location = l.location
        return move
