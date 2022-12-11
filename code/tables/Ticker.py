from dataclasses import dataclass,field


@dataclass
class Ticker():
    _symbol:str=field(init=False,repr=False)
    _open_time:int=field(init=False,repr=False)          ## Open time
    _open_price:str=field(init=False,repr=False)         ## Open
    _close_price:str=field(init=False,repr=False)        ## High
    _high_price:str=field(init=False)         ## Low
    _low_price:str=field(init=False)          ## Close
    _volume:str=field(init=False,repr=False)             ## Volume
    _close_time:int=field(init=False,repr=False)         ## Close Time
    _quote_asset_volume:str=field(init=False,repr=False) ## NMI
    _taker_buy_base:str=field(init=False,repr=False)     ## Taker buy base asset volume
    _taker_buy_asset:str=field(init=False,repr=False)    ## Taker buy quote asset volume
    _useded:str=field(init=False,repr=False)             ## Not used
    _loaded:bool=field(init=False,repr=False)

    def price_check(self,price:float):
        if float(self._low_price)<= price and \
                price <=float(self._high_price):
            return True
        else:
            return False

    @property
    def high_price(self): 
        print(self._high_price)
        return self._high_price


    @property
    def low_price(self): return self._low_price
