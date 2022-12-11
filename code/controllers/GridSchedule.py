from common.BaseClass import BaseClass
from abc import ABC,abstractmethod
from tables.TradeSymbol import TradeSymbol
import yaml
import traceback
class YamlFailure(Exception):
    def __init__(self):
        self.msg = 'Yaml file failed to load'
        super().__init__(self.msg)  

class GridSchedule(ABC):

    def __init__(self,bc:BaseClass)->None:
        self._bc=bc
        self._orders=[]

    @abstractmethod
    def ticker(self):
        pass

    @abstractmethod
    def setup_grid_orders(self):
        pass
    
    @abstractmethod
    def trade_wait(self):
        pass

    def setup_trades(self,yaml_file:str)->None:
        try:
            with open(yaml_file,'r') as file:
                trade=yaml.safe_load(file)
                for token in trade['Trades']:
                    for trade_pair in token['SymbolPair']:
                        trade_symbol=TradeSymbol()
                        trade_symbol.parse_data(token,trade_pair)
                        self.setup_grid_orders(trade_symbol)
        except:
            raise YamlFailure()

    def run_trades2(self):
        counter=0
        try:
            while True:
                for trade_pair in self._orders:
                    ticker=self.ticker()
                    trade_pair.reconciliation(ticker)
                    last_ticker=ticker
                counter+=1
                if counter >100:
                    break
                self.trade_wait()
        except IOError as e:
            self._bc.log.error('\t:'+traceback.format_exc())
        except:
            self._bc.log.error('\t:'+traceback.format_exc())
        finally:
            pass
