from common.BaseClass import BaseClass
from tables.TickerFile import TickerFile
from models.BinanceTicker import BinanaceTicker
import traceback

class EndOfTickers(Exception):
    def __init__(self):
        self.msg = 'Could not get a ticker.'
        super().__init__(self.msg)

class BinanaceTickerFile(BinanaceTicker):
    def __init__(self,bc:BaseClass,symbol:str):
        self._bc=bc
        self._symbol=symbol

    def parse_ticker(self,record,):
        ticker=TickerFile()
        ticker.parse_ticker(record)
        return ticker
