from order import Order

# This is an Initializer:
class Customer:
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
        if not isinstance(value, str) or len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = value

# Here we have an Object Relationship Method:
    def create_order(self, coffee, price):  
        if not isinstance(price, (int, float)) or price < 1.0 or price > 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        order = Order(self, coffee, price)  
        self._orders.append(order)  
        coffee._orders.append(order)  
        return order

# Here we have Object Relationship Properties:
    def orders(self):  
        return self._orders

    def coffees(self):  
        return list(set(order.coffee for order in self._orders))

# Here we have an Aggregate Method:
    @classmethod
    def most_aficionado(cls, coffee):  
        if not coffee.orders():  
            return None
        customer_spending = {}  
        for order in coffee.orders():
            if order.customer not in customer_spending:
                customer_spending[order.customer] = 0
            customer_spending[order.customer] += order.price  
        most_spent_customer = max(customer_spending, key=customer_spending.get)  
        return most_spent_customer