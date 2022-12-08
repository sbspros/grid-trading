from dataclasses import dataclass,field
import uuid

@dataclass
class Order():
    _symbol:str=field(init=False,repr=False)
    _client_order_id:int=field(init=False,repr=False)
    _order_list_id:int=field(init=False,repr=False)
    _client_order_id:str=field(init=False)
    _price:str=field(init=False,repr=False)
    _buy_price:str="0.0000"
    _sell_price:str="0.0000"
    _profit:str="0.0000"
    _orig_qty:str=field(init=False)
    _execute_qty:str=field(init=False,repr=False)
    _cummulative_quote_qyt:str=field(init=False,repr=False)
    _status:str=field(init=False,repr=False)
    _time_in_force:str=field(init=False,repr=False)
    _order_type:str=field(init=False,repr=False)
    _side:str='No Action'   ##Binance has buy and sell, I will be addind pending and,complete
    _stop_price:str=field(init=False,repr=False)
    _iceberg_qty:str=field(init=False,repr=False)
    _order_time:int=field(init=False,repr=False)
    _update_time:int=field(init=False,repr=False)
    _is_working:bool=field(init=False,repr=False)
    _orig_quote_order_qty:str=field(init=False,repr=False)

    def add(self,symbol,buy_price,sell_price:float,qty):
        self._symbol=symbol
        self._side='pending'
        self._buy_price=buy_price
        self._sell_price="{sell:.3f}".format(sell=sell_price)
        self._client_order_id=uuid.uuid4().hex
        self._orig_qty=qty
        return float(self._orig_qty)*float(self._buy_price)

    def sell(self):
        if self._side=='buy':
            self._side='complete'
            self._profit=str(\
                (float(self._sell_price)-float(self._buy_price))*float(self._orig_qty))
            return {'profit':(self._profit),'return_amount':float(self._sell_price)*float(self._orig_qty)}
            # afterwards add the money taken out code
        return {'profit':0.0,'return_amount':0.0}

    def buy(self):
        if self._side=='pending':
            self._side='buy'
        # afterwards add the money taken out code

    def side(self):
        return self._side
