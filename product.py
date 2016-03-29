# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Template']


class Template:
    __metaclass__ = PoolMeta
    __name__ = 'product.template'
    review_location = fields.Boolean('Review Location',
        help='Move to review location when receive supplier shipments')
