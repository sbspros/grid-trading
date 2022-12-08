from common.BaseClass import BaseClass
from models.BinanceConnection import BinanceConnection
from models.BinanceTestTrade import BinanceConnection
from decimal import Decimal as D, ROUND_DOWN, ROUND_UP
import decimal
import traceback


import os

class TradeFailed(Exception):
    def __init__(self):
        self.msg = 'Could not place test trade.'
        super().__init__(self.msg)

class BinanceTrade():
    def __init__(self,bc:BaseClass,conn:BinanceConnection,run_mode:str):
        self._bc=bc
        self._conn=conn
        self._run_mode=run_mode

    def trade(self,symbol:str,side:str,order_type:str,time_forced:str,qty:float,price:float):
        try:
            ## Fix QTY
            info = self._conn._client.get_symbol_info(symbol)
            quotePrecision = info['quotePrecision']
            quantityB = "{:0.0{}f}".format(qty, quotePrecision)
            priceB = "{:0.0{}f}".format(price, quotePrecision)

            if self._run_mode=="Test":
                order = self._conn._client.create_test_order(
                  symbol=symbol,
                  side=side,
                  type=order_type,
                  timeInForce='GTC',
                  quantity=quantityB,
                  price=priceB )
                return order
            else:
                raise "Mode Error"
                # return self._conn.client.create_order(
                #   symbol=symbol,
                #   side=side,
                #   type=order_type,
                #   timeInForce=time_forced,
                #   quantity=qty,
                #   price=price)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise TradeFailed()



# {
#     'symbol': 'SOLUSDT',
#     'status': 'TRADING',
#     'baseAsset': 'SOL',
#     'baseAssetPrecision': 8,
#     'quoteAsset': 'USDT',
#     'quotePrecision': 8,
#     'quoteAssetPrecision': 8,
#     'baseCommissionPrecision': 8,
#     'quoteCommissionPrecision': 8,
#     'orderTypes': ['LIMIT', 'LIMIT_MAKER', 'MARKET', 'STOP_LOSS_LIMIT', 'TAKE_PROFIT_LIMIT'],
#     'icebergAllowed': True,
#     'ocoAllowed': True,
#     'quoteOrderQtyMarketAllowed': True,
#     'allowTrailingStop': True,
#     'cancelReplaceAllowed': True,
#     'isSpotTradingAllowed': True,
#     'isMarginTradingAllowed': True,
#     'filters': [
#             {'filterType': 'PRICE_FILTER', 'minPrice': '0.01000000', 'maxPrice': '10000.00000000', 'tickSize': '0.01000000'},
#             {'filterType': 'PERCENT_PRICE', 'multiplierUp': '5', 'multiplierDown': '0.2', 'avgPriceMins': 5},
#             {'filterType': 'LOT_SIZE', 'minQty': '0.01000000', 'maxQty': '90000.00000000', 'stepSize': '0.01000000'},
#             {'filterType': 'MIN_NOTIONAL', 'minNotional': '10.00000000', 'applyToMarket': True, 'avgPriceMins': 5},
#             {'filterType': 'ICEBERG_PARTS', 'limit': 10},
#             {'filterType': 'MARKET_LOT_SIZE', 'minQty': '0.00000000', 'maxQty': '102688.00787623', 'stepSize': '0.00000000'},
#             {'filterType': 'TRAILING_DELTA', 'minTrailingAboveDelta': 10, 'maxTrailingAboveDelta': 2000, 'minTrailingBelowDelta': 10, 'maxTrailingBelowDelta': 2000},
#             {'filterType': 'MAX_NUM_ORDERS', 'maxNumOrders': 200}, {'filterType': 'MAX_NUM_ALGO_ORDERS', 'maxNumAlgoOrders': 5}],
#     'permissions': ['SPOT', 'MARGIN', 'TRD_GRP_005']}
