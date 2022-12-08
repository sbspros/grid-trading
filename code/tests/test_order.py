from tables.Order import Order

def test_add()->None:
    order=Order()
    order.add('SOLUSDT',\
              '15.000',\
              '15.500','3')
    assert order._side=='pending'

def test_sell_wout_buy()->None:
    order=Order()
    order.add('SOLUSDT',\
              '15.000',\
              '15.500','3')
    order.sell()
    assert order._side=='pending'

def test_sell()->None:
    order=Order()
    order.add('SOLUSDT',\
              '15.000',\
              '15.500','3')
    order.buy()
    order.sell()
    assert order._side=='complete'

def test_buy()->None:
    order=Order()
    order.add('SOLUSDT',\
              '15.000',\
              '15.500','3')
    order.buy()
    assert order._side=='buy'


def test_buy_wout_pend()->None:
    order=Order()
    order.add('SOLUSDT',\
              '15.000',\
              '15.500','3')
    order.buy()
    order.sell()
    order.buy()
    assert order._side!='buy'

