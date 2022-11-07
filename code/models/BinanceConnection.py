from common.BaseClass import BaseClass
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import traceback
import os

class BinanceConnectionFailed(Exception):
    def __init__(self):
        self.msg = 'Count not connect to Binance'
        super().__init__(self.msg)    

class BinanceConnection():
     def __init__(self,bc:BaseClass):
         self._bc=bc
         try:
            self._client = Client(os.environ.get('BINANCE_API'), os.environ.get('BINANCE_SECERT'))
            self._bc.log.info("\tConnected to Binance")
         except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise BinanceConnectionFailed()