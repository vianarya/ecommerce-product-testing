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


def find_product_by_category(category):
    results = [p for p in product_db if p["category"].lower() == category.lower()]
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


# ─────────────────────────────────────────────
# FIND BY CATEGORY TEST CASES
# ─────────────────────────────────────────────

def test_find_product_by_exact_category():
    """Test finding products by exact category name."""
    save_product(make_product(name="Laptop", category="Electronics"))
    save_product(make_product(name="Phone", category="Electronics"))

    results = find_product_by_category("Electronics")

    assert len(results) == 2
    for result in results:
        assert result["category"] == "Electronics"


def test_find_product_by_category_case_insensitive():
    """Test that category search is case-insensitive."""
    save_product(make_product(name="T-Shirt", category="Clothing"))

    results = find_product_by_category("clothing")

    assert len(results) == 1
    assert results[0]["category"] == "Clothing"


def test_find_product_by_category_not_found():
    """Test that searching for a non-existent category returns empty list."""
    save_product(make_product(name="Laptop", category="Electronics"))

    results = find_product_by_category("Furniture")

    assert results == []


def test_find_product_by_category_returns_only_matching():
    """Test that only products in the specified category are returned."""
    save_product(make_product(name="Laptop", category="Electronics"))
    save_product(make_product(name="T-Shirt", category="Clothing"))
    save_product(make_product(name="Phone", category="Electronics"))

    results = find_product_by_category("Electronics")

    assert len(results) == 2
    for result in results:
        assert result["category"] == "Electronics"


def test_find_product_by_category_empty_string():
    """Test searching with an empty category returns empty list."""
    save_product(make_product(name="Laptop", category="Electronics"))

    results = find_product_by_category("")

    assert results == []


def test_find_product_by_category_multiple_categories():
    """Test finding products across different categories."""
    save_product(make_product(name="Book", category="Books"))
    save_product(make_product(name="Novel", category="Books"))
    save_product(make_product(name="Laptop", category="Electronics"))

    books = find_product_by_category("Books")
    electronics = find_product_by_category("Electronics")

    assert len(books) == 2
    assert len(electronics) == 1
