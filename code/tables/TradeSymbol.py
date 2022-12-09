from dataclasses import dataclass, field
@dataclass
class TradeSymbol():
    _token:str=field(init=False)
    _base_cur:str=field(init=False,repr=False)
    _invest_amount:str=field(init=False)
    _pairs:list=field(init=False,default_factory=list)
    _symbol:str=field(init=False,repr=False)
    _base_pair:str=field(init=False)
    _upper_limit:str=field(init=False)
    _lower_limit:str=field(init=False)
    _price_step:str=field(init=False)
    _buy_amount:str=field(init=False)
    _file_name:str=field(init=False)
    _pending_depth:int=field(init=False,default=0)
    _max_pending_depth:int=0
    _spent:float=0.0
    _tokens:float=0.0
    _war_chest:float=0.0
    _return_amount:float=0.0

    def parse_data(self,symbol,trade_info)->None:
        self._token=symbol['Token']
        self._invest_amount=trade_info['InvestAmount']
        self._war_chest=float(trade_info['InvestAmount'])
        self._base_pair=trade_info['BaseCur'],
        self._upper_limit=trade_info['UpperLimit'],
        self._lower_limit=trade_info['LowerLimit'],
        self._price_step=trade_info['PriceStep'],
        self._buy_amount=trade_info['BuyAmount'],
        self._max_pending_depth=int(trade_info['MaxPendingDepth'])
        self._file_name=trade_info['FileName']

    def update_total(selfi,profit,action_cost,action):
        self._symbol_info.total_profit+=profit
        if action==Sell:
            self._symbol_info._war_chest+=action_value
            self._symbol_info._tokens-=self._symbol_info._buy_amount
    
    def investment_summary(selfi,last_ticker):
        self._bc.log.error(trade_pair._)
        self._bc.log.info("")
        self._bc.log.info("Total float cash \t\t${float_cash:6.3f}".format(float_cash=self._war_chest))
        self._bc.log.info("Pending order return \t${return_amount:6.3f}".format(return_amount=self._return_amount))
        self._bc.log.info("Tokens own \t\t\t{tokens:3.3f} (${close_price})".format(tokens=self._tokens,close_price=last_ticker._close_price))
        self._bc.log.info("Investment value \t\t${cash:6.2f} ".format(\
                                cash=self._return_amount+self._war_chest+\
                                self._tokens*float(last_ticker._close_price)))
