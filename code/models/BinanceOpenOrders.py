from common.BaseClass import BaseClass
from models.BinanceConnection import BinanceConnection
import traceback
import os

class OpenOrdersFailed(Exception):
    def __init__(self):
        self.msg = 'Count not connect to order book.'
        super().__init__(self.msg)  
        
class BinanceOpenOrders():
    def __init__(self,bc:BaseClass,conn:BinanceConnection):
        self._bc=bc
        self._conn=conn

    def open_orders(self,symbol:str):
        try:
            return self._conn._client.get_open_orders(symbol=symbol)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise OrderbookFailed()           