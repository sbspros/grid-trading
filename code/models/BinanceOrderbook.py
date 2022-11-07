from common.BaseClass import BaseClass
from models.BinanceConnection import BinanceConnection
import traceback
import os

class OrderbookFailed(Exception):
    def __init__(self):
        self.msg = 'Count not connect to order book.'
        super().__init__(self.msg)  
        
class BinanceOrderbook():
    def __init__(self,bc:BaseClass,conn:BinanceConnection):
        self._bc=bc
        self._conn=conn

    def order_book(self,symbol:str):
        try:
            return self._conn._client.get_historical_trades(symbol=symbol)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise OrderbookFailed()           