import pytest

def update_price(products):
    for product in products:
        product['price'] *= 1.15
    return products

@pytest.fixture
def products():
    return [
        {'name': 'Product 1', 'price': 100},
        {'name': 'Product 2', 'price': 200},
        {'name': 'Product 3', 'price': 300}
    ]

def test_update_price(products):
    updated_products = update_price(products)
    assert updated_products[0]['price'] == 115
    assert updated_products[1]['price'] == 230
    assert updated_products[2]['price'] == 345

def test_update_price_empty_list():
    assert update_price([]) == []

def test_update_price_no_price_key():
    products = [{'name': 'Product 1'}, {'name': 'Product 2'}]
    with pytest.raises(KeyError):
        update_price(products)
