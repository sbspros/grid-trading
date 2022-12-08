from common.BaseClass import BaseClass
from tables.GridOrder import GridOrder
from tables.TradeSymbol import TradeSymbol
from tables.TickerFile import TickerFile

def test_no_orders()->None:
    ##this is an init case with no other orders current in the system
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


