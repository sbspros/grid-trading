from common.BaseClass import BaseClass
from models.BinanceConnection import BinanceConnection,BinanceConnectionFailed
from models. BinanceCandles import  BinanceCandles,CandleStickFailed

import traceback

class GridSetupFailure(Exception):
    def __init__(self):
        self.msg = 'Could not setup grids.'
        super().__init__(self.msg)

class SetupGrids():
    last_time=-2
    def __init__(self,bc:BaseClass,conn:BinanceConnection,\
        token:str,interval:str,war_chess:float,num_of_grids:int):
        self._bc=bc
        self._conn=conn
        self._token=token
        self._interval=interval
        self._num_of_grids=num_of_grids
        self._war_chess=war_chess*.5
        self._range=self.cal_range()
        print(self._range)
        self._price_step=self._range/self._num_of_grids
        #self._buy_amount=self._war_chess/self._num_of_grids
        self._buy_amount=688.0/self._num_of_grids  

    def cal_range(self):
        candles= BinanceCandles(self._bc,self._conn)
        candle_list=candles.candle_stick(self._token,self._interval)
        candle=candles.get_candle(SetupGrids.last_time)
        print(candle['high']+' '+candle['low'])
        self._high=float(candle['high'])
        self._low=float(candle['low'])
        return abs(float(candle['high'])-float(candle['low']))
    
    def init_setup(self):
        return {
            'price_step':self._price_step,
            'buy_amount':self._buy_amount,
            'starting_investment':self._war_chess,
            'high':self._high,
            'low':self._low,
        }
