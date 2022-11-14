from common.BaseClass import BaseClass
from models.BinanceConnection import BinanceConnection
from models.BinanceTicker import BinanceTicker
from models.BinanceTrade import BinanceTrade,TradeFailed
from models.BinanceOpenOrders import BinanceOpenOrders,OpenOrdersFailed
from objects.PendingOrders import PendingOrders
from objects.Orders import Orders
from binance.enums import *
import uuid


class GridPairs():
    run_mode='Test'
    def __init__(self,bc:BaseClass,\
            conn:BinanceConnection,\
            token:str,base_cur:str,\
            investment_amount:float,\
            upper_limit:float,lower_limit:float,\
            price_steps:float,buy_amount:float,run_mode:str ):
        self._bc=bc
        self._conn=conn
        self._orders=[]
        ## a token is the crypto currency being trade
        self._token=token
        ## base currency is what the token is trade un
        self._base_cur=base_cur
        self._api_symbol=self._token+self._base_cur
        self._investment_amount=investment_amount
        self._upper_limit=upper_limit
        self._lower_limit=lower_limit
        self._price_step=price_steps
        self._buy_amount=buy_amount
        self._trade=BinanceTrade(self._bc,self._conn,run_mode)
        self._ticker=BinanceTicker(self._bc,self._conn)
        self._active_orders={}
        self._pending_orders=PendingOrders(bc)
        self._orders_test=Orders(bc)
    
    @property    
    def api_symbol(self):return self._api_symbol
        
    ## used to get the existing order for the api_symbol
    def get_existing_order(self):
        self._bc.log.error("\t Inside get existing orders")
        open_orders=BinanceOpenOrders(self._bc,self._conn)
        tmp_list=open_orders.open_orders(self.api_symbol)
        self._orders=sorted( tmp_list, key=lambda d: d['price'],reverse=True)
        for order in self._orders:
            self._pending_orders.add_order(order)
            
            
    def reconciliation2(self):
        self._bc.log.error("\t reconciliation order")
        ticker_price=float(self._ticker.ticker(self.api_symbol)['bidPrice'])            
        found_order=False
        uuid_check=uuid.uuid4()
        for order in PendingOrders.pending_orders:
            ## Check for missing orders
            self._pending_orders.check_order(uuid_check,order)
            
            ## do we need a new buy order
            if order['price']<= ticker and ticker <=order['top_price']:
                self._bc.log.error("\t Found pending buy order for price {price}".format(price=ticker))
                found_order=True
            
            ## do a order get trigger and needs removing
            if ticker>order['sell_price'] and order['side']=='sell':
                self._bc.log.error("\t Found pending sell order for price {price}".format(price=ticker))
                self._pending_orders.delete_order(order)
                
        if not found_order and self._investment_amount >self._buy_amount*ticker_price :
            self._bc.log.error("\t Buying an order")
            ## the BinanceBuyOrder will have a flag for calling the test system buy and live buys
            self._trade.trade(\
                self.api_symbol,SIDE_BUY,ORDER_TYPE_LIMIT,TIME_IN_FORCE_GTC,self._buy_amount,ticker_price-self._price_step)
            #print(self._orders[-1])
            self._pending_orders.pending_orders.add_buy({
                'orderId':uuid.uuid4().hex,
                'symbol': self._api_symbol,
                'side':'buy',
                'qty': self._buy_amount,
                'price' : ticker_price-self._price_step
            })
            
        for order in self._pending_orders.missing_order(uuid_check):
            self._orders.append(self._trade.trade(\
                order.symbol,SIDE_SELL,ORDER_TYPE_LIMIT,TIME_IN_FORCE_GTC,order.executedQt,order.price+self._price_step))    

    # ## Removes orders than have been sold.
    # def reconciliation(self):
    #     self._bc.log.error("\t reconciliation order")
    #     ticker_price=float(self._ticker.ticker(self.api_symbol)['bidPrice'])
         
    #     list_len=len(Orders.pending_orders) 6
    #     ## add sort logic here from high to low
    #     found_order=False
    #     uuid_check=uuid.uuid4()
    #     print(list_len)
    #     for i in range(0,list_len):
    #         print(i)
    #         self._pending_orders.check_order(uuid_check,self._orders[i]['orderId'])

    #         if i>0 and \
    #             float(Orders.pending_orders[i-1]['price'])>=ticker_price and \
    #             ticker_price >=float(Orders.pending_orders[i]['price'])<= ticker_price:
    #             found_order=True

    #     if not found_order and self._investment_amount >self._buy_amount*ticker_price :
    #         self._bc.log.error("\t Buying an order")
    #         ## the BinanceBuyOrder will have a flag for calling the test system buy and live buys
    #         self._trade.trade(\
    #             self.api_symbol,SIDE_BUY,ORDER_TYPE_LIMIT,TIME_IN_FORCE_GTC,self._buy_amount,ticker_price-self._price_step)
    #         #print(self._orders[-1])
    #         self._pending_orders.add_sell({
    #             'orderId':uuid.uuid4().hex,
    #             'symbol': self._api_symbol,
    #             'side':'sell'
    #             'qty': self._buy_amount,
    #             'price' : ticker_price-self._price_step
    #         })
            
    #         Orders.pending_orders.add_order({
    #             'orderId':uuid.uuid4().hex,
    #             'side':'buy'
    #             'symbol': self._api_symbol,
    #             'qty': self._buy_amount,
    #             'price' : ticker_price-self._price_step,
    #             'sell_price':ticker_price
    #         })
    
    #     for order in self._pending_orders.missing_order(uuid_check):
    #         self._orders.append(self._trade.trade(\
    #             order.symbol,SIDE_SELL,ORDER_TYPE_LIMIT,TIME_IN_FORCE_GTC,\
    #                 order.executedQt,order.price+self._price_step))