from common.BaseClass import BaseClass
from models.BinanceConnection import BinanceConnection
from models.BinanceTestTrade import BinanceConnection
import traceback


import os

class TradeFailed(Exception):
    def __init__(self):
        self.msg = 'Could not place test trade.'
        super().__init__(self.msg)  
        
class BinanceTrade():
    
    def __init__(self,bc:BaseClass,conn:BinanceConnection,run_mode:str):
        self._bc=bc
        self._conn=conn
        self._run_mode=run_mode

    def trade(self,symbol:str,side:str,order_type:str,time_forced:str,qyt:float,price:float):
        try:
            if self._run_mode=="Test":
                return self._conn._client.client.create_test_order(
                  symbol=symbol,
                  side=side,
                  type=order_type,
                  timeInForce=time_forced,
                  quantity=qty,
                  price=price)                
            else:
                raise "Mode Error"
                return self._conn._client.client.create_order(
                  symbol=symbol,
                  side=side,
                  type=order_type,
                  timeInForce=time_forced,
                  quantity=qty,
                  price=price)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise TradeFailed() 
