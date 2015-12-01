# This file is part of the stock_shipment_review module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockShipmentReviewTestCase(ModuleTestCase):
    'Test Stock Shipment Review module'
    module = 'stock_shipment_review'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockShipmentReviewTestCase))
    return suite