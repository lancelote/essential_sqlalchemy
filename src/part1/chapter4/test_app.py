from decimal import Decimal

import pytest

from src.part1.chapter4.app import get_orders_by_customer
from src.part1.chapter4.db import dal, prepare_db


@pytest.fixture(scope='module', autouse=True)
def database():
    dal.db_init('sqlite:///:memory:')
    prepare_db()


def test_orders_by_blank_customer_name():
    results = get_orders_by_customer('')
    assert results == []


def test_orders_by_blank_customer_name_shipped():
    results = get_orders_by_customer('', shipped=True)
    assert results == []


def test_orders_by_blank_customer_name_not_shipped():
    results = get_orders_by_customer('', shipped=False)
    assert results == []


def test_orders_by_blank_customer_name_details():
    results = get_orders_by_customer('', details=True)
    assert results == []


def test_orders_by_blank_customer_name_shipped_details():
    results = get_orders_by_customer('', shipped=True, details=True)
    assert results == []


def test_orders_by_blank_customer_name_not_shipped_details():
    results = get_orders_by_customer('', shipped=False, details=True)
    assert results == []


def test_orders_by_customer():
    expected_result = [('wlk001', 'cookiemon', '111-111-1111')]
    results = get_orders_by_customer('cookiemon')
    assert results == expected_result


def test_order_by_customer_shipped_only():
    results = get_orders_by_customer('cookiemon', True)
    assert results == []


def test_orders_by_customer_unshipped_only():
    expected_results = [('wlk001', 'cookiemon', '111-111-1111')]
    results = get_orders_by_customer('cookiemon', False)
    assert results == expected_results


def test_orders_by_customer_with_details():
    expected_results = [
        ('wlk001', 'cookiemon', '111-111-1111', 'dark chocolate chip', 2, Decimal('1.00')),
        ('wlk001', 'cookiemon', '111-111-1111', 'oatmeal raisin', 12, Decimal('3.00'))
    ]
    results = get_orders_by_customer('cookiemon', details=True)
    assert results == expected_results


def test_orders_by_customer_shipped_only_with_details():
    results = get_orders_by_customer('cookiemon', True, True)
    assert results == []


def test_orders_by_customer_unshipped_only_details():
    expected_results = [
        ('wlk001', 'cookiemon', '111-111-1111', 'dark chocolate chip', 2, Decimal('1.00')),
        ('wlk001', 'cookiemon', '111-111-1111', 'oatmeal raisin', 12, Decimal('3.00'))
    ]
    results = get_orders_by_customer('cookiemon', shipped=False, details=True)
    assert results == expected_results
