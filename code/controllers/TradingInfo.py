from common.BaseClass import BaseClass
from models.BinanceConnection import BinanceConnection,BinanceConnectionFailed
from controllers.TradeSetup import TradeSetup
import traceback
import os

class TradeInfoFailure(Exception):
    def __init__(self):
        self.msg = 'Count not connect to order book.'
        super().__init__(self.msg)  
        
class TradeInfo():
    price='price'
    def __init__(self,bc:BaseClass,conn:BinanceConnection,token:str,base_pair:str,step_amount:float,qty:float):
        self._bc=bc
        self._conn=conn
        self._token=token
        self._base_pair=base_pair
        self._step_amount=step_amount
        self._qty=qty
        trade_setup=TradeSetup(self._bc,self._conn,self._token,self._base_pair)
        self._setup=trade_setup.startup_values()

        
    def setup_new_trades(self):
        
        current_price_break=float(self._setup["order_list"][0][TradeInfo.price])+self._step_amount
        order_queue=[]
        times=0
        while current_price_break <float(self._setup["price"]):

            order_queue.append({
                "Status":"Pending-Buy",
                "price":current_price_break,
                "qty":qty_amount
            })
            times=times+1
            if times>50:
                raise "Loop Trigger"
            current_price_break=current_price_break+step_amount
        self._setup['additional_orders']=order_queue
        return self._setup            
