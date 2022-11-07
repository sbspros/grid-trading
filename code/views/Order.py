from common.BaseClass import BaseClass
class Order():
    
    def __init__(self,bc:BaseClass,order:[],price:str):
        self._bc=bc
        self._order=order
        self._price=float(price)
    
    def __str__(self):
        return "Order {type} for price {price} and qty {qty} current Total {total}:"\
            .format(type=self._order['side'],price=self._order['price'],qty=self._order['origQty'],total=float(self._order['origQty'])*self._price)