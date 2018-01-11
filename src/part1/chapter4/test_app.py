import unittest

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
