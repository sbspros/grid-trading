from tables.Ticker import Ticker

class TickerFile(Ticker):


    def parse_ticker(self,ticker):
        self._symbol=ticker[10]
        self._open_time=ticker[0]
        self._open_price=ticker[4]
        self._close_price=ticker[3]
        self._high_price=ticker[2]
        self._low_price=ticker[1]
        self._volume=ticker[5]
        self._close_time=ticker[6]
        self._quote_asset_volume=ticker[7]
        self._taker_buy_base=ticker[8]
        self._taker_buy_asset=ticker[9]

    @property
    def high_price(self): 
        return float(self._high_price)

    @property
    def low_price(self): return float(self._low_price)
