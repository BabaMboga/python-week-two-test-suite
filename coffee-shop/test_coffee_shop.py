import pytest
from customer import Customer
from coffee import Coffee
from order import Order

# Testing Customer Class
def test_customer_name_validatoin():
    # Valid name
    customer1 = Customer("Alice")
    assert customer1.name == "Alice"

    #Name length validation (1-15 characters)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("A" * 16)

def test_customer_orders_and_coffees():
    customer1 = Customer("Bob")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")

    # Initially no orders

    assert customer1.orders() == []
    assert customer1.coffees() == []

    # create orders
    customer1.create_order(coffee1, 4.5)
    customer1.create_order(coffee2, 5.0)

    #Verify the orders and coffess
    assert len(customer1.orders()) == 2
    assert set(customer1.coffees()) == {coffee1, coffee2}

# Testing Coffee Class
def test_coffee_name_validation():
    # Valid name
    coffee1 = Coffee("Latte")
    assert coffee1.name == "Latte"

    # Name length validation (at least 3 characters)
    with pytest.raises(ValueError):
        Coffee("A")

def test_coffee_orders_customers():
    coffee1 = Coffee("Cappucino")
    customer1 = Customer("Dave")
    customer2 = Customer("Eve")

    #Initially no orders

    assert coffee1.orders() == []
    assert coffee1.customers() == []

    # Create orders
    customer1.create_order(coffee1, 6.0)
    customer2.create_order(coffee1, 5.5)

    # Verify orders and customers
    assert len(coffee1.orders()) == 2
    assert set(coffee1.customers()) == {customer1, customer2}

def test_coffee_num_orders_and_average_price():
    coffee1 = Coffee("Americano")
    customer1 = Customer("John")

    #No orders initially 
    assert coffee1.num_orders() == 0
    assert coffee1.average_price() == 0

    #create orders
    customer1.create_order(coffee1, 5.0)
    customer1.create_order(coffee1, 6.0)

    #Test num_orders and average_price
    assert coffee1.num_orders() == 2
    assert coffee1.average_price() == 5.5

#Testing Order Class
def test_order_creation_and_validation():
    customer1 = Customer("Alice")
    coffee1 = Coffee("Mocha")

    #Valid order
    order1 = Order(customer1, coffee1, 3.5)
    assert order1.customer == customer1
    assert order1.coffee == coffee1
    assert order1.price == 3.5

    # Price validation (must be between 1.0 and 10.0)
    with pytest.raises(ValueError):
        Order(customer1, coffee1, 0.5)
    with pytest.raises(ValueError):
        Order(customer1, coffee1, 11.0)

def run_tests():
    test_coffee_name_validation()
    test_customer_orders_and_coffees()
    test_coffee_name_validation()
    test_coffee_orders_customers()
    test_coffee_num_orders_and_average_price()
    test_order_creation_and_validation()


if __name__ == "__main__":
    run_tests()