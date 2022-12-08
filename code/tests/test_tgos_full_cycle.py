from common.BaseClass import BaseClass
from tables.GridOrder import GridOrder
from tables.TradeSymbol import TradeSymbol
from tables.TickerFile import TickerFile

def test_full_cycle()->None:
    ## This starts with no order and does a full cycle from pending to
    ## complete

    ## Create init order
    order=GridOrder()

    ## Create a ticker outside of range
    ticker=TickerFile()

    ## init test case, get an order
    ticker.parse_ticker([1,'99.67','99.82','99.50','99.67',\
                         'vol',2,'vol2','vol3','vol4','-2'])

    ##Since there are not order the first check is no action
    ## becase there is nothing to action against
    assert order.check_order(ticker)=='No Action'
    order.add('SOLUSDT','99.50','99.75','0.82')
    assert order._buy_price=='99.50'
    assert order._side=='pending'


    ## The buy price is betweeb the tickers low and high
    ## buy was triggered
    ticker.parse_ticker([1,'99.43','100.20','99.61','100.17',\
                         'vol',2,'vol2','vol3','vol4','-2'])
    assert order.check_order(ticker)=='Buy'
    assert ticker._low_price=='99.43'
    assert order._buy_price=='99.50'
    assert order._sell_price=='99.75'
    assert ticker._high_price=='100.20'
    assert order._side=='pending'
    order.buy()
    assert order._side=='buy'


    ## The sell price is betweeb the tickers low and high
    ## sellwas triggered
    ticker.parse_ticker([1,'99.43','100.20','99.61','100.17',\
                         'vol',2,'vol2','vol3','vol4','-2'])
    assert order.check_order(ticker)=='Sell'
    assert ticker._low_price=='99.43'
    assert order._buy_price=='99.50'
    assert order._sell_price=='99.75'
    assert ticker._high_price=='100.20'
    assert order._side=='buy'
    order.sell()
    assert order._side=='complete'

