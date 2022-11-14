import uuid
class Orders():
    pending_orders={}
    
    def __init__(self,bc):
        self._bc=bc
        
    def add_order(self,order):

        if order!={}:
            uuid_check=uuid.uuid4().hex
            Orders.pending_orders[uuid_check]=order
       
    def delete_order(self,order):
        Orders.pending_orders.pop([order['orderId']])
    
    def open_order(self):
        orders=[]
        for order in Orders.pending_orders:
            orders.append(order)
        return orders
    