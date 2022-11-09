from common.BaseClass import BaseClass,AppException
from models.BinanceConnection import BinanceConnection,BinanceConnectionFailed
from controllers.TradingInfo import TradeInfo
from controllers.SetupGrids import SetupGrids
from controllers.SchTrade import SchTrade
from objects.GridPairs import GridPairs
from views.Order import Order
import traceback
import sched
from time import time, sleep
import yaml

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"


if __name__ == "__main__":        
    bc=BaseClass('config.ini')
    bc.log.info("Start of app")
    
    try:
        
        ## Try to connect to the Binace Server
        connection=BinanceConnection(bc)
        with open('yaml/starting.yaml', 'r') as file:
            trades = yaml.safe_load(file) 
  
        pairs=[]
        for trade in trades['Trades']:
            print(trade)
            pairs.append(GridPairs(bc,\
                connection,\
                trade['Token'],trade['BaseCur'],\
                trade['InvestAmount'],\
                trade['UpperLimit'],trade['LowerLimit'],\
                trade['PriceStep'],trade['BayAmount']))
	    pairs[-1].get_open_orders
	     
            
        x=1
        while x<100:
            for trade_grid in pairs:
                trade_grid.create_order()
            x=x+1

	
	
        while True:
	
        #     sleep(60 - time() % 60)
	    #     # thing to run
        #     trading.check_for_trade()
        #     loop_count=loop_counter+1
        #     if loop_count >10000:break
    except:
        bc.log.error("\t"+":"+traceback.format_exc())
        print("Applicaton fail to start.  Review the log file.")
