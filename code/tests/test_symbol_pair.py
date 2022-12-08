
from tables.SymbolPair import SymbolPair

def test_symbol_pair()->None:
    symbol_pair=SymbolPair('USDT','15.50','12.50','0.3','0.86')
    assert symbol_pair._base_pair=='USDT'
    assert symbol_pair._upper_limit=='15.50'
