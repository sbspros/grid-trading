from tables.TickerWeb import TickerWeb

def test_parse_ticker()->None:
    ticker=TickerWeb()
    ticker.parse_ticker([1,'5','6','7','4',\
                         'vol',2,'vol2','vol3','vol4','-2'])
    assert ticker._open_price=='5'

def test_price_check()->None:
    ticker=TickerWeb()
    ticker.parse_ticker([1,'5','6','7','4',\
                         'vol',2,'vol2','vol3','vol4','-2'])
    assert ticker.price_check(5.5)==True
    assert ticker.price_check(8.5)==False

