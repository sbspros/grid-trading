from controllers.GridSchedule import GridSchedule
from common.BaseClass import BaseClass
from table.TradeSymbol import TradeSymbol
from models.BinanceConnection import BinanceConnection
from controllers.GridOrders import GridOrders
import time
import traceback
class BinanceGridTrading(GridSchedule):

    def __init__(self,bc:BaseClass,trade_setup:[])->None:
        super().__init__(bc,trade_setup)

    def trade_wait(self):
        time.sleep(60)

    def ticker(self):
        ## Get a ticker from Binance
        ## use self._conn to get the data

        pass

    def setup_grid_orders(self,trade_symbol:TradeSymbol):
        self._orders.append(GridOrders(self._bc,self._conn,trade_symbol)


    def binance_connection(self)
        self._conn= "Something"
