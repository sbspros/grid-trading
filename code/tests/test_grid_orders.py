from controllers.GridOrders import GridOrders
from common.BaseClass import BaseClass
from tables.TradeSymbol import TradeSymbol
from tables.TickerFile import TickerFile

def test_grid_orders()->None:
    ## init the GridOrders

    bc=BaseClass('config.ini')
    filename='data/SOLUSDT-1m-2022-03.csv'
    symbol=TradeSymbol()
    symbol.parse_data({
        "Token":"SOL",\
        "InvestAmount":"600'00",\
        "SymbolPair":[{
        "BaseCur":"USDT",\
        "UpperLimit":"15.000",\
        "LowerLimit":"12.500",\
        "PriceStep":"0.140",\
        "BuyAmount":"0.8200"}]})
    grid_orders=GridOrders(bc,None,symbol,True)
    assert len(grid_orders._orders)==0
    assert grid_orders._orders==[]
    assert grid_orders._conn==None
    assert grid_orders._test_mode==True
    ticker=TickerFile()
    ticker.parse_ticker([1,'99.67','99.82','99.50','99.67',\
                         'vol',2,'vol2','vol3','vol4','-2'])

    grid_orders.reconciliation(ticker)
    assert len(grid_orders._orders)==1
    assert grid_orders.side()=='pending'
