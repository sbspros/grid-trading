from tables.TradeSymbol import TradeSymbol
from tables.SymbolPair import SymbolPair

def  test_pasre_data()->None:
    symbol=TradeSymbol()
    symbol.parse_data({
        "Token":"SOL",\
        "InvestAmount":"600'00",\
        "SymbolPair":[{
        "BaseCur":"USDT",\
        "UpperLimit":"15.000",\
        "LowerLimit":"12.500",\
        "PriceStep":"0.140",\
        "BuyAmount":"0.8200"}]})
    assert symbol._token=='SOL'

