from common.BaseClass import BaseClass
from abc import ABC,abstractmethod
from tables.GridOrder import GridOrder
from tables.Ticker import Ticker
from tables.TradeSymbol import TradeSymbol
class GridOrders(ABC):
    run_mode='Test'
    total_profit=0.0
    def __init__(self,bc:BaseClass,\
            symbol_info:TradeSymbol,\
            )->None:
        self._bc=bc
        self._symbol_info=symbol_info
        self._orders=[]
    
    @abstractmethod
    def new_order(self):
        pass

    @abstractmethod
    def cancel_pending(self):
        pass

    def sell(self):
        values=self._orders[order].sell()
        self._symbol_info.update_totals(float(values['profit']),value['return_amount'],'Sell')
        self.log_action('Sell   ',self._orders[order],ticker,GridOrders.total_profit)

    def buy(self):
        self._orders[order].buy()
        self._symbol_info.update_totals(0.0,0.0,'Buy')
        self.log_action('Buy    ',self._orders[order],ticker,GridOrders.total_profit)

    def found_order(self):
        found_order=True

    def cancel_pending_orders(self,last_ticker):
        return_amount=0.0
        self._bc.log.error('inside cancel orders')
        num_of_orders=len(self._orders)
        if num_of_orders >=1:
            for order in range(0,num_of_orders):
                if self._orders[order]._side=='pending':
                    self._bc.log.error(str(self._orders[order]))
                    self._symbol_info._return_amount+=float(self._orders[order]._buy_price)*float(self._orders[order]._orig_qty)


    def reconciliation(self,ticker:Ticker):
        if self.symbol_info._lower_limit> ticker._high_price and  \
                self._symbol_info.upper_limit < ticker._low_price:
                    return
        found_order=False
        action='No Orders'
        num_of_orders=len(self._orders)
        if num_of_orders >=1:
            for order in range(0,num_of_orders):
                ## do we need a new buy order
                action=self._orders[order].check_order(ticker)
                if action=='Sell':
                    self.sell()
                elif action=='Buy':
                    self.buy()
                elif action=='Found':
                    found_order=True
                    self.found_order()
                    ## self.log_action('Found  ',self._orders[order],ticker,GridOrders.total_profit)
        if not found_order:
            self.new_order()
        return action

    def log_action(self,action:str,order:GridOrder,ticker:Ticker,total_profit:float)->None:
        self._bc.log.debug("{uuid},{action:8s},{ticker_high:7.2f},{ticker_low:7.2f},{order_buy:7.2f},{order_sell:7.2f},{amount:5.2f},{status:8s},{profit:5.2f},{total_profit:5.2f},{tokens:8.3f},{war_chest:7.2f},{current:7.2f}"\
                          .format(action=action,\
                                  ticker_high=float(ticker._high_price),\
                                  ticker_low=float(ticker._low_price),\
                                  order_buy=float(order._buy_price),\
                                  order_sell=float(order._sell_price),\
                                  amount=order._orig_qty,\
                                  status=order._side,\
                                  profit=float(order._profit),\
                                  uuid=order._client_order_id[-3],\
                                  total_profit=float(total_profit),\
                                  tokens=self._symbol_info._tokens,\
                                  war_chest=self._symbol_info._war_chest,
                                  current=self._symbol_info._war_chest+(self._symbol_info._tokens*float(ticker._close_price))
                                  ))
