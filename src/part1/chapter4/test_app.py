import unittest
from decimal import Decimal

from src.part1.chapter4.app import get_orders_by_customer
from src.part1.chapter4.db import dal, prepare_db


class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        dal.db_init('sqlite:///:memory:')
        prepare_db()

    def test_orders_by_blank_customer_name(self):
        results = get_orders_by_customer('')
        self.assertEqual(results, [])

    def test_orders_by_blank_customer_name_shipped(self):
        results = get_orders_by_customer('', shipped=True)
        self.assertEqual(results, [])

    def test_orders_by_blank_customer_name_not_shipped(self):
        results = get_orders_by_customer('', shipped=False)
        self.assertEqual(results, [])

    def test_orders_by_blank_customer_name_details(self):
        results = get_orders_by_customer('', details=True)
        self.assertEqual(results, [])

    def test_orders_by_blank_customer_name_shipped_details(self):
        results = get_orders_by_customer('', shipped=True, details=True)
        self.assertEqual(results, [])

    def test_orders_by_blank_customer_name_not_shipped_details(self):
        results = get_orders_by_customer('', shipped=False, details=True)
        self.assertEqual(results, [])

    def test_orders_by_customer(self):
        expected_result = [('wlk001', 'cookiemon', '111-111-1111')]
        results = get_orders_by_customer('cookiemon')
        self.assertEqual(results, expected_result)

    def test_order_by_customer_shipped_only(self):
        results = get_orders_by_customer('cookiemon', True)
        self.assertEqual(results, [])

    def test_orders_by_customer_unshipped_only(self):
        expected_results = [('wlk001', 'cookiemon', '111-111-1111')]
        results = get_orders_by_customer('cookiemon', False)
        self.assertEqual(results, expected_results)

    def test_orders_by_customer_with_details(self):
        expected_results = [
            ('wlk001', 'cookiemon', '111-111-1111', 'dark chocolate chip', 2, Decimal('1.00')),
            ('wlk001', 'cookiemon', '111-111-1111', 'oatmeal raisin', 12, Decimal('3.00'))
        ]
        results = get_orders_by_customer('cookiemon', details=True)
        self.assertEqual(results, expected_results)

    def test_orders_by_customer_shipped_only_with_details(self):
        results = get_orders_by_customer('cookiemon', True, True)
        self.assertEqual(results, [])

    def test_orders_by_customer_unshipped_only_details(self):
        expected_results = [
            ('wlk001', 'cookiemon', '111-111-1111', 'dark chocolate chip', 2, Decimal('1.00')),
            ('wlk001', 'cookiemon', '111-111-1111', 'oatmeal raisin', 12, Decimal('3.00'))
        ]
        results = get_orders_by_customer('cookiemon', shipped=False, details=True)
        self.assertTrue(results, expected_results)
