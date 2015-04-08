# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['ShipmentOut']
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
