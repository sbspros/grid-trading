from common.BaseClass import BaseClass,AppException
from controllers.BinanceGridSchedule import BinanceGridSchedule
import time
import traceback
import yaml

if __name__=="__main__":
    bc=BaseClass('config.ini')
    try:
        trading=BinanceGridSchedule(bc)
        trading.setup_trades('yaml/starting.yaml')
        trading.binace_connection()
        trading.run_trades()
    except:
        bc.log.error('\t:'+traceback.format_exc())
        print('Application fail to start. Review the log file')
