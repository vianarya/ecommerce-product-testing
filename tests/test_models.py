import pytest
from tests.factories import make_product, make_products


# Simulated in-memory product database
product_db = []


def save_product(product):
    product_db.append(product)
    return product


def find_product_by_name(name):
    results = [p for p in product_db if p["name"].lower() == name.lower()]
    return results


def setup_function():
    """Clear DB before each test."""
    product_db.clear()


# ─────────────────────────────────────────────
# FIND BY NAME TEST CASES
# ─────────────────────────────────────────────

def test_find_product_by_exact_name():
    """Test finding a product by its exact name."""
    product = make_product(name="Wireless Headphones")
    save_product(product)

    results = find_product_by_name("Wireless Headphones")

    assert len(results) == 1
    assert results[0]["name"] == "Wireless Headphones"


def test_find_product_by_name_case_insensitive():
    """Test that search is case-insensitive."""
    product = make_product(name="Bluetooth Speaker")
    save_product(product)

    results = find_product_by_name("bluetooth speaker")

    assert len(results) == 1
    assert results[0]["name"] == "Bluetooth Speaker"


def test_find_product_by_name_returns_multiple():
    """Test finding multiple products with the same name."""
    save_product(make_product(name="USB Cable"))
    save_product(make_product(name="USB Cable"))

    results = find_product_by_name("USB Cable")

    assert len(results) == 2


def test_find_product_by_name_not_found():
    """Test that searching for a non-existent name returns empty list."""
    save_product(make_product(name="Laptop Stand"))

    results = find_product_by_name("Keyboard")

    assert results == []


def test_find_product_by_name_empty_string():
    """Test searching with an empty string returns nothing useful."""
    save_product(make_product(name="Smart Watch"))

    results = find_product_by_name("")

    assert results == []


def test_find_product_by_name_among_multiple_products():
    """Test finding the correct product when multiple products exist."""
    save_product(make_product(name="Phone Case"))
    save_product(make_product(name="Screen Protector"))
    save_product(make_product(name="Charging Dock"))

    results = find_product_by_name("Screen Protector")

    assert len(results) == 1
    assert results[0]["name"] == "Screen Protector"
