from common.BaseClass import BaseClass
from models.BinanceConnection import BinanceConnection
import traceback
import os

class AssetBalanceFailed(Exception):
    def __init__(self):
        self.msg = 'Count not connect to order book.'
        super().__init__(self.msg)  
        
class BinanceAssetBalance():
    def __init__(self,bc:BaseClass,conn:BinanceConnection):
        self._bc=bc
        self._conn=conn

    def asset_balance(self,asset):
        try:
            return self._conn._client.get_asset_balance(asset=asset)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise AccoutnInfoFailed()           