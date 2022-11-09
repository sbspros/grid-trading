from common.BaseClass import BaseClass
from models.BinanceConnection import BinanceConnection




class GridPairs():
    def __init__(self,bc:BaseClass,\
            conn:BinanceConnection,\
            token:str,base_cur:str,\
            investment_amount:float,\
            upper_limit:float,lower_limit:float,\
            price_steps:float,buy_amount:float ):
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
        self._price_steps=price_steps
        self._buy_amount=buy_amount
    
    @property    
    def api_symbol(self):return self._api_symbol
        
    ## used to get the existing order for the api_symbol
    def get_existing_order(self):
        self._bc.log.error("\t Inside get existing orders")
        pass
    
    ## gets current price and loops to see if there are existing orders
    ## if not, it creates one
    def create_order(self):
        self._bc.log.error("\t Creates order if needed")
        pass
    
    ## Removes orders than have been sold.
    def remove_order(self):
        self._bc.log.error("\t Creates order if needed")
        pass
    
    """ 
def get_open_orders(self,orders):
	## the main controller gets open orders and pass it into method
	## it reduces the calls to Binance and speeds up the process
	- for order in orders:
		-order[‘status’]=‘live’
		-if order[‘symbol’]==self.api_symbol:
			-self._open_orders.append(order)

-def reconcyle_orders
	-ticket_price=Ticker(self.api_symbol)
	-list_len=len(self._open_orders)
	-## add sort logic here from high to low
	- found_order=False
	-for i in range(0,list_len):
		-if ticker_price >self._open_orders[i][‘buy_price’] and \
			-self._open_order[i][‘staus’]==‘live’:
			self._open_orders[i][‘status’]=‘sold’
		If i>0 and self._open_orders[i][‘price’]>=ticker_price and \
			-self._open_orders[i-1]<= ticker_price:
			-found_order=True
	-if not found_order and self._investment_amount >self._buy_amount*ticker_price :
		## the BinanceBuyOrder will have a flag for calling the test system buy and live buys
		-self._open_order.append(BinanceBuyOrder(\
			-self.api_symbol,self._step_amount,self._buy_amount*ticker_price)

This simplifies the main controller into something like
	# after reading the yaml file
	For grid_pair in grid_pairs:
		grid_pair.get_orders()
	While true
		For grid_pair in grid_pairs:
			grid_pair.reconcycle _order()
		wait 60 seconds """
    
    