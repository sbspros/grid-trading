from common.BaseClass import BaseClass
from models.BinanceConnection import BinanceConnection
import traceback
import os

class CandleStickFailed(Exception):
    def __init__(self):
        self.msg = 'Could not connect to candle sticks.'
        super().__init__(self.msg)  
        
class BinanceCandles():

    high=2
    low=3
    open=1
    close=4

    def __init__(self,bc:BaseClass,conn:BinanceConnection):
        self._bc=bc
        self._conn=conn

    def candle_stick(self,symbol:str,interval:str):
        try:
            self._candle_list = self._conn._client.get_klines(symbol=symbol, interval=interval)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise CandleStickFailed() 

    def get_candle(self,which_one):
        return {'high':self._candle_list[which_one][BinanceCandles.high],\
            'low':self._candle_list[which_one][BinanceCandles.low],\
            'open':self._candle_list[which_one][BinanceCandles.open],\
            'close':self._candle_list[which_one][BinanceCandles.close]}   