from controllers.GridSchedule import GridSchedule
from common.BaseClass import BaseClass
from models.BinanceTicker import BinanceTicker,EndOfTickers
from controllers.GridOrdersFile import GridOrdersFile
from tables.TradeSymbol import TradeSymbol
import traceback
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


