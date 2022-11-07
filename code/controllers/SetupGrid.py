from common.BaseClass import BaseClass
from models.BinanceConnection import BinanceConnection,BinanceConnectionFailed
from models. BinanceCandles import  BinanceCandles,CandleStickFailed

import traceback

class GridSetupFailure(Exception):
    def __init__(self):
        self.msg = 'Could not setup grids.'
        super().__init__(self.msg)

class SetupGrids():
    def __init__(self,bc:BaseClass,conn:BinanceConnection,token:str,interval:str):
        self._bc=bc
        self._conn=conn
        self._token=token
        self._interval=interval
        
    def cal_interval(self):
        candles=
    
        
        
