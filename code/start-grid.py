from common.BaseClass import BaseClass,AppException
from models.BinanceConnection import BinanceConnection,BinanceConnectionFailed
from controllers.TradingInfo import TradeInfo
from controllers.SchTrade import SchTrade
from views.Order import Order
import traceback
import sched
from time import time, sleep

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
    qty_amount=0.62
    step_amount=0.30
    
    try:
        
        ## Try to connect to the Binace Server
        connection=BinanceConnection(bc)
        
        ## Get Account Updates
        trade_info=TradeInfo(bc,connection,'SOL','USDT',step_amount,qty_amount)
    
        trades_starter=trade_info.setup_new_trades()       
    except BinanceConnectionFailed as e:
        print("Applicaton fail to start.  Review the log file.")
        
    except:
        bc.log.error("\t"+":"+traceback.format_exc())
        print("Applicaton fail to start.  Review the log file.")
    
    ## Start the trading
    try:
        trading=SchTrade(bc,connection,\
        trades_starter['war_chess'],\
        trades_starter['price'],\
        trades_starter['additional_orders'],step_amount,qty_amount)
        loop_counter=0
        trading.check_for_trade()
        while True:
            sleep(60 - time() % 60)
	        # thing to run
            trading.check_for_trade()
            loop_count=loop_counter+1
            if loop_count >10000:break
    except:
        bc.log.error("\t"+":"+traceback.format_exc())
        print("Applicaton fail to start.  Review the log file.")