# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .configuration import *
from .shipment import *


def register():
    Pool.register(
        ConfigurationLocation,
        Configuration,
        ShipmentOut,
        module='stock_shipment_review', type_='model')
