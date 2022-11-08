from common.BaseClass import BaseClass,AppException
from models.BinanceConnection import BinanceConnection,BinanceConnectionFailed
from models.BinanceOrderbook import BinanceOrderbook,OrderbookFailed
from models.BinanceOpenOrders import BinanceOpenOrders,OpenOrdersFailed
from models.BinanceAssetBalance import BinanceAssetBalance, AssetBalanceFailed
from views.Order import Order
import traceback
import os

class TradeSetupFailure(Exception):
    def __init__(self):
        self.msg = 'Count not connect to order book.'
        super().__init__(self.msg)  
        
class TradeSetup():
    price='price'
    free='free'
    def __init__(self,bc:BaseClass,conn:BinanceConnection,token,base_pair):
        self._bc=bc
        self._conn=conn
        self._token=token
        self._base_pair=base_pair

    def startup_values(self):
    
        ## Get a list of all customers recent orders
        orderbook=BinanceOrderbook(self._bc,self._conn)
        
        ## Top one has a price
        self._price=orderbook.order_book(self._token+self._base_pair)[0][TradeSetup.price]
        
        ## Get how much crypto cash I have
        account=BinanceAssetBalance(self._bc,self._conn)
        asset=account.asset_balance(self._base_pair)
        print(asset)
        self._free_asset=asset[TradeSetup.free]
        
        #Get open orders
        self.open_orders()
        
        ## Where is price
        self.where_is_price()
        
        
        return{
            "price_at":self._price_at,
            "order_list":self._order_list,
            "war_chess":self._free_asset,
            "price":float(self._price),}

    def open_orders(self):
        ##  Get my open orders
        orders=BinanceOpenOrders(self._bc,self._conn)
        tmp_order_list=orders.open_orders(self._token+self._base_pair)
        self._order_list= sorted(tmp_order_list, key=lambda d: d[TradeSetup.price],reverse=True)
    
    def where_is_price(self):
        ## Find out where price is in that list
        printed=False
        self._price_at=0        
        for order in self._order_list:
            if float(self._price) >float(order[TradeSetup.price]) and printed==False:
                printed=True
            elif printed==False:
                self._price_at=self._price_at+1
           