from tables.Order import Order
from tables.Ticker import Ticker
class GridOrder(Order):

    def check_order(self,ticker:Ticker)->str:
        action='No Action'
        if self._side!='complete':
            ## Do we need to buy
            if self._side=='pending' and\
                    float(ticker._low_price) <= float(self._buy_price) and\
                    float(self._buy_price) <= float(ticker._high_price):
                #buy order was triggered
                action='Buy'
            elif self._side=='buy' and\
                    float(ticker._low_price) <= float(self._sell_price) and\
                    float(self._sell_price) <= float(ticker._high_price):
                action='Sell'
            elif self._side=='buy' and\
                    float(ticker._low_price) <= float(self._buy_price) and\
                    float(self._buy_price) <= float(ticker._high_price):
                action='Found'

        return action

