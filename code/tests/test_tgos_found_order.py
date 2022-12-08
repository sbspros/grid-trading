from common.BaseClass import BaseClass
from tables.GridOrder import GridOrder
from tables.TradeSymbol import TradeSymbol
from tables.TickerFile import TickerFile

def test_found_order()->None:
    ## This case is to put a pending buy in and have a ticker that stays
    ## within that pending buy causing a Found and No Action to happen

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
    order.add('SOLUSDT','99.50','199.50','0.82')
    assert order._buy_price=='99.50'
    assert order._side=='pending'


    ## init test case, get an order
    ticker.parse_ticker([1,'99.67','99.82','99.50','99.67',\
                         'vol',2,'vol2','vol3','vol4','-2'])
    ##Since there are not order the first check is no action
    ## becase there is nothing to action against
    assert ticker._low_price=='99.67'
    assert order._sell_price=='199.50'
    assert ticker._high_price=='99.82'
    assert order.check_order(ticker)=='No Action'
    assert order._side=='pending'

