from controllers.GridSchedule import GridSchedule
from common.BaseClass import BaseClass
from models.BinanceTicker import BinanceTicker,EndOfTickers
from controllers.GridOrdersFile import GridOrdersFile
from tables.TradeSymbol import TradeSymbol
import traceback
import csv
## This will read a SQLite3 table containing ticker data and run it through
## the Grid Trading Logic

class GridScheduleFile(GridSchedule):


    def __init__(self,bc:BaseClass)->None:
        super().__init__(bc)


    def trade_wait(self):
        pass
    

    def ticker(self):
        pass

    def setup_grid_orders(self,trade_symbol:TradeSymbol):
        self._orders.append(GridOrdersFile(self._bc,trade_symbol))


    def run_trades(self):
        counter=0
        for trade_pair in self._orders:
            self._bc.log.error(str(trade_pair._symbol_info._file_name))
            try:
                with open(trade_pair._symbol_info._file_name) as csvFile:
                    for row in csv.reader(csvFile,delimiter=','):
                        self._bc.log.error(row)
            except IOError as e:
                self._bc.log.error("\t"+":"+traceback.format_exc())
                raise CSVReadException()
            except:
                self._bc.log.error("\t"+":"+traceback.format_exc())
                raise AppException()
