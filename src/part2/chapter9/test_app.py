import unittest
from decimal import Decimal

from src.part2.chapter9.app import get_order_by_customer
from src.part2.chapter9.db import dal, prep_db


class TestApp(unittest.TestCase):
    cookie_orders = [(1, 'cookiemon', '111-111-1111')]
    cookie_details = [
        (1, 'cookiemon', '111-111-1111', 'dark chocolate chip', 2, Decimal('1.00')),
        (1, 'cookiemon', '111-111-1111', 'oatmeal raisin', 12, Decimal('3.00'))
    ]

    @classmethod
    def setUpClass(cls):
        dal.connect('sqlite:///:memory:')
        prep_db(dal.session)
        dal.session.close()

    def setUp(self):
        dal.restart_session()

    def tearDown(self):
        dal.session.rollback()
        dal.session.close()

    def test_orders_by_customer_blank(self):
        results = get_order_by_customer('')
        self.assertEqual(results, [])

    def test_orders_by_customer_blank_shipped(self):
        results = get_order_by_customer('', True)
        self.assertEqual(results, [])

    def test_orders_by_customer_blank_not_shipped(self):
        results = get_order_by_customer('', False)
        self.assertEqual(results, [])

    def test_orders_by_customer_blank_details(self):
        results = get_order_by_customer('', details=True)
        self.assertEqual(results, [])

    def test_orders_by_customer_blank_shipped_details(self):
        results = get_order_by_customer('', True, True)
        self.assertEqual(results, [])

    def test_orders_by_customer_blank_not_shipped_details(self):
        results = get_order_by_customer('', False, True)
        self.assertEqual(results, [])

    def test_order_by_customer(self):
        results = get_order_by_customer('cookiemon')
        self.assertEqual(results, self.cookie_orders)

    def test_orders_by_customer_shipped_only(self):
        results = get_order_by_customer('cookiemon', False)
        self.assertEqual(results, self.cookie_orders)

    def test_orders_by_customer_with_details(self):
        results = get_order_by_customer('cookiemon', details=True)
        self.assertEqual(results, self.cookie_details)

    def test_orders_by_customer_shipped_only_with_details(self):
        results = get_order_by_customer('cookiemon', True, True)
        self.assertEqual(results, [])

    def test_orders_by_customer_not_shipped_only_details(self):
        results = get_order_by_customer('cookiemon', False, True)
        self.assertEqual(results, self.cookie_details)
