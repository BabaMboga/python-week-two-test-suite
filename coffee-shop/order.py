# order.py
# This is an Initializer:
class Order:
    def __init__(self, customer, coffee, price):
        
        # Validate price input
        if not isinstance(price, (int, float)) or price < 1.0 or price > 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._customer = customer  
        self._coffee = coffee  
        self._price = price  

# These are Properties:
    @property
    def customer(self):  
        return self._customer

    @property
    def coffee(self):  
        return self._coffee

    @property
    def price(self):  
        return self._price