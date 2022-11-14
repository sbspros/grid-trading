import uuid
class PendingOrders():
    pending_orders={}
    
    def __init__(self,bc):
        self._bc=bc
        
    def add_sell(self,order):

        if order!={}:
            uuid_check=uuid.uuid4().hex
            PendingOrders.pending_orders[uuid_check]=order
            #print(PendingOrders.pending_orders)
        
    def check_order(self,uuid_check,orderId):
        try:
            PendingOrders.pending_orders[orderId]['uuid']=uuid
        except:
            pass
        
    def missing_order(self,uuid):
        orders=[]
        for order_key in  PendingOrders.pending_orders:
            try:
                if PendingOrders.pending_orders['uuid']!=uuid:
                    orders.append(order)
                    PendingOrders.pending_orders.pop(order['orderId'])
            except KeyError:
                pass
        return orders