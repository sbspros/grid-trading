from common.BaseClass import BaseClass
from models.BinanceConnection import BinanceConnection
import traceback
import os

class CancelOrderFailed(Exception):
    def __init__(self):
        self.msg = 'Count not connect to order book.'
        super().__init__(self.msg)  
        
class BinanceCancelOrder():
    def __init__(self,bc:BaseClass,conn:BinanceConnection):
        self._bc=bc
        self._conn=conn

    def cancel_order(self,symbol:str, order_id:str):
        try:
            return self._conn._client.get_order(symbol=symbol,orderId=order_id)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise CancelOrderFailed()               
