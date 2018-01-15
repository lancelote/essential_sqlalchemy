import unittest
from decimal import Decimal
from unittest import mock

from src.part1.chapter4.app import get_orders_by_customer


class TestApp(unittest.TestCase):
    cookie_orders = [('wlk001', 'cookiemon', '111-111-1111')]
    cookie_details = [
        ('wlk001', 'cookiemon', '111-111-1111', 'dark chocolate chip', 2, Decimal('1.00')),
        ('wlk001', 'cookiemon', '111-111-1111', 'oatmeal raisin', 12, Decimal('3.00')),
    ]

    @mock.patch('src.part1.chapter4.app.dal.connection')
    def test_orders_by_customer(self, mock_connection):
        mock_connection.execute.return_value.fetchall.return_value = self.cookie_orders
        results = get_orders_by_customer('cookiemon')
        self.assertEqual(results, self.cookie_orders)

    @mock.patch('src.part1.chapter4.app.select')
    @mock.patch('src.part1.chapter4.app.dal.connection')
    def test_orders_by_customer_blank(self, mock_connection, mock_select):
        mock_select.return_value.select_from.return_value.where.return_value = ''
        mock_connection.execute.return_value.fetchall.return_value = []
        results = get_orders_by_customer('')
        self.assertEqual(results, [])
