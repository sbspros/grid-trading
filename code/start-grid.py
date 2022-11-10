from common.BaseClass import BaseClass,AppException
from models.BinanceConnection import BinanceConnection,BinanceConnectionFailed
from models.BinanceOrderbook import BinanceOrderbook
from models.BinanceAccountInfo import BinanceAccountInfo, AccountInfoFailed
from models.BinanceAssetBalance import BinanceAssetBalance,AssetBalanceFailed
from objects.GridPairs import GridPairs
import traceback
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

	## How much money do I have to spend
	account_balance=BinanceAssetBalance()
	war_chest=account_balance.asset_balance('USDT')
	
	## Get all open orders
	orderbook=BinanceOrderbook(self._bc,self._conn)
        with open('yaml/starting.yaml', 'r') as file:
            trades = yaml.safe_load(file)
	
        ## not using BinanceAccountInfo, why not
        pairs=[]
        for trade in trades['Trades']:
            print(trade)
            pairs.append(GridPairs(bc,\
                connection,\
                trade['Token'],trade['BaseCur'],\
                trade['InvestAmount'],\
                trade['UpperLimit'],trade['LowerLimit'],\
                trade['PriceStep'],trade['BayAmount']))
	    pairs[-1].get_open_orders(orderbook)
	while True:
	    for grid_pair in pairs:
		grid_pair.reconciliation()
	    sleep(60 - time() % 60)
    except:
        bc.log.error("\t"+":"+traceback.format_exc())
        print("Applicaton fail to start.  Review the log file.")
