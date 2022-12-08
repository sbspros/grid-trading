from common.BaseClass import BaseClass
from data_reader.CSVReader import CSVReader, CSVReadException,\
    CSVOpenException
from models.BinanceConnection import BinanceConnection
from tables.TickerWeb import TickerWeb
from tables.TickerFile import TickerFile
import traceback
import os

class TickerFailed(Exception):
    def __init__(self):
        self.msg = 'Could not get a ticker.'
        super().__init__(self.msg)

class EndOfTickers(Exception):
    def __init__(self):
        self.msg = 'Could not get a ticker.'
        super().__init__(self.msg)

class BinanceTicker():
    def __init__(self,bc:BaseClass,conn:BinanceConnection,symbol:str,file_name:str=None):
        self._bc=bc
        self._conn=conn
        self._symbol=symbol

    def ticker(self,symbol:str):
        try:
            for tick in self._conn._client.get_orderbook_tickers():
                if tick['symbol']==symbol:
                    return(tick)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise TickerFailed()


    def next_record(self,symbol,row):
        ##Check to see if there is a next reocrd
        try:
            return self.parse_ticker(row,symbol)
        except IndexError as e:
            self._bc.log.error('Last record process')
            raise EndOfTickers()
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())

    def parse_ticker(self,record,symbol):
        ticker=TickerFile()
        ticker.parse_ticker(record,symbol)
        return ticker
