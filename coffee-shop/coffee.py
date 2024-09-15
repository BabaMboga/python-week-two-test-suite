# coffee.py

# This is an Initializer:
class Coffee:
    def __init__(self, name):  
        self._name = None
        self.name = name  
        self._orders = []  

# These are Properties:
    @property
    def name(self):  
        return self._name

    @name.setter
    def name(self, value):  
        if not isinstance(value, str) or len(value) < 3:  
            raise ValueError("Name must be a string with at least 3 characters.")
        self._name = value  

# Here we have Object Relationship Properties:
    def orders(self):  
        return self._orders

    def customers(self):  
        return list(set(order.customer for order in self._orders))

# Here we have Aggregate Methods:
    def num_orders(self):  
        return len(self._orders)

    def average_price(self):  
        if not self._orders:  
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)   