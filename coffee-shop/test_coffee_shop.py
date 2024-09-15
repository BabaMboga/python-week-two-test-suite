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

def test_customer_orders_and_coffess():
    customer1 = Customer("Bob")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")

    # Initially no orders

    assert customer1.orders() == []
    assert customer1.coffess() == []

    # create orders
    customer1.create_order(coffee1, 4.5)
    customer1.create_order(coffee2, 5.0)

    #Verify the orders and coffess
    assert len(customer1.orders()) == 2
    assert set(customer1.coffees) == {coffee1, coffee2}

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

