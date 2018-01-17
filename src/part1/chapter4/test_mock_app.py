from src.part1.chapter4 import app
from src.part1.chapter4.app import dal, get_orders_by_customer


def test_orders_by_customer(mocker):
    mocker.patch.object(dal, 'connection')
    cookie_orders = [('wlk001', 'cookiemon', '111-111-1111')]
    dal.connection.execute.return_value.fetchall.return_value = cookie_orders
    assert get_orders_by_customer('cookiemon') == cookie_orders


def test_orders_by_customer_blank(mocker):
    mocker.patch.object(dal, 'connection')
    mocker.patch.object(app, 'select')
    dal.connection.execute.return_value.fetchall.return_value = []
    app.select.return_value.select_from.return_value.where.return_value = ''
    assert get_orders_by_customer('') == []
