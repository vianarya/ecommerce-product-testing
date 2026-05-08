import factory
from faker import Faker

fake = Faker()


class ProductFactory(factory.Factory):
    class Meta:
        model = dict

    id = factory.Sequence(lambda n: n + 1)
    name = factory.LazyFunction(lambda: fake.catch_phrase())
    description = factory.LazyFunction(lambda: fake.text(max_nb_chars=200))
    price = factory.LazyFunction(lambda: round(fake.pyfloat(min_value=1, max_value=1000, right_digits=2), 2))
    stock = factory.LazyFunction(lambda: fake.random_int(min=0, max=500))
    category = factory.LazyFunction(lambda: fake.random_element(elements=[
        "Electronics",
        "Clothing",
        "Books",
        "Home & Garden",
        "Sports",
        "Toys",
        "Beauty",
        "Automotive",
    ]))
    sku = factory.LazyFunction(lambda: fake.bothify(text="SKU-####-???").upper())
    image_url = factory.LazyFunction(lambda: fake.image_url())
    is_active = factory.LazyFunction(lambda: fake.boolean(chance_of_getting_true=80))
    created_at = factory.LazyFunction(lambda: fake.date_time_this_year().isoformat())


class InvalidProductFactory(factory.Factory):
    """Factory for generating invalid/edge-case product data for negative testing."""

    class Meta:
        model = dict

    id = None
    name = ""
    description = None
    price = factory.LazyFunction(lambda: fake.random_element(elements=[-1, 0, None, "abc"]))
    stock = factory.LazyFunction(lambda: fake.random_element(elements=[-5, None, "invalid"]))
    category = "Unknown"
    sku = ""
    image_url = "not-a-valid-url"
    is_active = None
    created_at = None


def make_product(**kwargs):
    """Helper to create a single fake product dict."""
    return ProductFactory(**kwargs)


def make_products(count=5, **kwargs):
    """Helper to create multiple fake product dicts."""
    return [ProductFactory(**kwargs) for _ in range(count)]


def make_invalid_product(**kwargs):
    """Helper to create a single invalid product dict for negative testing."""
    return InvalidProductFactory(**kwargs)
