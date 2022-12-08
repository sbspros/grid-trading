from common.BaseClass import BaseClass,AppException
from controllers.GridScheduleFile import GridScheduleFile
import time
import traceback
import yaml

if __name__=="__main__":
    bc=BaseClass('config.ini')
    try:
        trading=GridScheduleFile(bc)
        trading.setup_trades('yaml/starting.yaml')
        trading.run_trades()
    except:
        bc.log.error('\t:'+traceback.format_exc())
        print('Application fail to start. Review the log file')
