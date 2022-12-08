from tables.GridOrder import GridOrder
from tables.TickerWeb import TickerWeb
from tables.Order import Order

def test_check_order_blank()->None:
    ## There are no orders
    order=GridOrder()

    ## Create a ticker outside of range
    ticker=TickerWeb()
    ticker.parse_ticker([1,'5','6','7','4',\
                         'vol',2,'vol2','vol3','vol4','-2'])

    assert order.check_order(ticker)=='No Action'

def test_check_order_no_action()->None:

    ## Test test an existing orderr
    ## Side should be pending
    order=GridOrder()
    order.add(symbol='SOLUSDT',buy_price='15.000',sell_price='15.500',qty='3')
    assert order._side=='pending'


    ## Create a ticker outside of range
    ticker=TickerWeb()
    ticker.parse_ticker([1,'5','6','14.98','4',\
                         'vol',2,'vol2','vol3','vol4','-2'])
    assert order.check_order(ticker)=='No Action'

def test_check_order_found()->None:
    ## Test with an existing orderr
    ## Side should be pending
    order=GridOrder()
    order.add(symbol='SOLUSDT',buy_price='15.000',sell_price='15.500',qty='3')
    assert order._side=='pending'

    ## Create a ticker around the buy price
    ticker=TickerWeb()
    ticker.parse_ticker([1,'5','6','15.05','14.9',\
                         'vol',2,'vol2','vol3','vol4','-2'])
    ## Need to put the order in a buy state
    order.buy()
    assert order._side=='buy'
    order.check_order(ticker)
    assert order.check_order(ticker)=='Found'

def test_check_order_sell()->None:

    ## Test with an existing orderr
    ## Side should be pending
    order=GridOrder()
    order.add(symbol='SOLUSDT',buy_price='15.000',sell_price='15.500',qty='3')
    assert order._side=='pending'

    #Setup ticker
    ticker=TickerWeb()
    ticker.parse_ticker([1,'5','6','15.55','14.9',\
                         'vol',2,'vol2','vol3','vol4','-2'])

    ## Need an existing order
    order.buy()
    assert order._side=='buy'
    assert order.check_order(ticker)=='Sell'
    order.sell()
    assert order._side=='complete'

def test_check_order_buy()->None:

    ## Test with an existing orderr
    ## Side should be pending
    order=GridOrder()
    order.add(symbol='SOLUSDT',buy_price='15.000',sell_price='15.500',qty='3')
    assert order._side=='pending'

    #Setup ticker
    ticker=TickerWeb()
    ticker.parse_ticker([1,'5','6','15.55','14.9',\
                         'vol',2,'vol2','vol3','vol4','-2'])

    assert order.check_order(ticker)=='Buy'
    order.buy()
    assert order._side=='buy'
