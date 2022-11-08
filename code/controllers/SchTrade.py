from common.BaseClass import BaseClass
from models.BinanceConnection import BinanceConnection,BinanceConnectionFailed
from models.BinanceTicker import BinanceTicker,TickerFailed
from controllers.TradeSetup import TradeSetup
import traceback

class SchTrade():
    def __init__(self,bc:BaseClass,conn:BinanceConnection,\
        war_chess,price,additional_orders,step_amount,qty_amount,upper_limit,lower_limit):
        self._bc=bc
        self._conn=conn
        self._war_chess=war_chess
        self._current_price=price
        self._additional_orders=additional_orders
        self._ticker=BinanceTicker(self._bc,self._conn)
        self._step_amount=step_amount
        self._qty_amount=qty_amount
        self._upper_limit=upper_limit
        self.lower_limit=lower_limit

    def check_for_trade(self):
        prices=self._ticker.ticker("SOLUSDT")
        self.create_buy_order(float(prices['bidPrice']),float(prices['bidPrice'])-2*self._step_amount)
        self.check_for_buy(float(prices['bidPrice']))
        
    def create_buy_order(self,price:float,lower_price:float):
        found=False
        for order in self._additional_orders:
            if price>order['buy-price'] and order['buy-price']>lower_price:
                found=True
        if not found:
            self._bc.log.error("Create buy order for {buy_price}".format(buy_price=price-self._step_amount))
            self._additional_orders.append({'buy-price':price-self._step_amount,'sell-price':price,'status':'pending-buy'})
            
    def check_for_buy(self,price):
        ## this is for testing
        for order in  self._additional_orders:
            if order['status']=='bought' and price >=order['sell-price']:
                order['status']='pending-buy'
                self._bc.log.error("Sold at  {buy_price}".format(buy_price=order['sell-price']))  
                          
            if order['status'] == 'pending-buy' and price <= order['buy-price']:
                order['status']='bought'
                self._bc.log.error("Bought order {buy_price}".format(buy_price=order['buy-price']))
                
            
            
        