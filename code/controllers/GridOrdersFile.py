from common.BaseClass import BaseClass
from controllers.GridOrders import GridOrders
from tables.Ticker import Ticker
from tables.TradeSymbol import TradeSymbol
class GridOrdersFile(GridOrders):
    
    def __init__(self,bc:BaseClass,trade_symbol:TradeSymbol)->None:
        super().__init__(bc,trade_symbol)

    def new_order(self,ticker:Ticker):
        new_order=GridFileOrder(ticker)
        cost=new_order.add(ticker._symbol,ticker._close_price,\
                        (float(self._symbol_info._price_step)+float(ticker._close_price)),  \
                                self._symbol_info._buy_amount)
        self._symbol_info.update_totals(0.0,cost,'Pending')
        self.log_action('Pending',new_order,ticker,self._symbol_info._total_profit)
        self._orders.append(new_order)
        self._symbol_info._pending_depth+=1


    def cancel_pending(self,last_ticker):
        return_amount=0.0
        self._bc.log.error('inside cancel orders')
        num_of_orders=len(self._orders)
        if num_of_orders >=1:
            for order in range(0,num_of_orders):
                if self._orders[order]._side=='pending':
                    self._bc.log.error(str(self._orders[order]))
                    self._symbol_info._return_amount+=float(self._orders[order]._buy_price)*float(self._orders[order]._orig_qty)


