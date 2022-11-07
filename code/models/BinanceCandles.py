from common.BaseClass import BaseClass
from models.BinanceConnection import BinanceConnection
import traceback
import os

class CandleStickFailed(Exception):
    def __init__(self):
        self.msg = 'Count not connect to candle sticks.'
        super().__init__(self.msg)  
        
class BinanceCandles():
    def __init__(self,bc:BaseClass,conn:BinanceConnection):
        self._bc=bc
        self._conn=conn

    def candle_stick(self,symbol:str,interval:str):
        try:
            return self._conn._client.get_klines(symbol=symbol, interval=interval):
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise TickerFailed()  
