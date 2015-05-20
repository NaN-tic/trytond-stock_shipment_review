# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields, ModelSQL, ModelView
from trytond.pool import PoolMeta
from trytond.pyson import If, Bool, Eval

__all__ = ['ConfigurationLocationReview', 'Configuration']
__metaclass__ = PoolMeta


class ConfigurationLocationReview(ModelSQL, ModelView):
    'Configuration Location Review'
    __name__ = 'stock.configuration.location.review'
    configuration = fields.Many2One('stock.configuration', 'Configuration',
        ondelete='CASCADE', select=True, required=True)
    warehouse = fields.Many2One('stock.location', 'Warehouse', required=True,
        domain=[('type', '=', 'warehouse')], ondelete='CASCADE')
    location = fields.Many2One('stock.location', 'Location', required=True,
        ondelete='CASCADE',
        domain=[
            ('type', '=', 'storage'),
            ('parent', 'child_of', If(Bool(Eval('warehouse')),
                    [Eval('warehouse')], [])),
            ], depends=['warehouse'], select=True)


class Configuration:
    __name__ = 'stock.configuration'
    review_locations = fields.One2Many('stock.configuration.location.review',
        'configuration', 'Review Locations')
