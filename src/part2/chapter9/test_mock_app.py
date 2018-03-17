import unittest
from decimal import Decimal
from unittest import mock

from src.part2.chapter9.app import get_order_by_customer


class TestApp(unittest.TestCase):
    cookie_orders = [(1, 'cookiemon', '111-111-1111')]
    cookie_details = [
        (1, 'cookiemon', '111-111-1111', 'dark chocolate chip', 2, Decimal('1.00')),
        (1, 'cookiemon', '111-111-1111', 'oatmeal raisin', 12, Decimal('3.00'))
    ]

    @mock.patch('src.part2.chapter9.app.dal.session')
    def test_orders_by_customer(self, mock_dal):
        mock_dal.query.return_value.join.return_value.filter.return_value. \
            all.return_value = self.cookie_orders
        results = get_order_by_customer('cookiemon')
        self.assertEqual(results, self.cookie_orders)
