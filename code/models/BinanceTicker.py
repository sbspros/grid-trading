from common.BaseClass import BaseClass
from models.BinanceConnection import BinanceConnection
import traceback
import os

class TickerFailed(Exception):
    def __init__(self):
        self.msg = 'Could not get a ticker.'
        super().__init__(self.msg)  
        
class BinanceTicker():
    def __init__(self,bc:BaseClass,conn:BinanceConnection):
        self._bc=bc
        self._conn=conn

    def ticker(self,symbol:str):
        try:
            for tick in self._conn._client.get_orderbook_tickers():
                if tick['symbol']==symbol:
                    return(tick)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise TickerFailed()           
