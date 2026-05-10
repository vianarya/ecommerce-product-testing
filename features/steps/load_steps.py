from behave import given
from tests.factories import make_product


# ─────────────────────────────────────────────
# BACKGROUND DATA LOADING STEP DEFINITIONS
# ─────────────────────────────────────────────

@given('the following products exist in the system')
def step_load_products_from_table(context):
    """Load background products from the feature file table into the system."""
    context.product_db = []
    for row in context.table:
        product = make_product(
            name=row["name"],
            price=float(row["price"]),
            category=row["category"],
            stock=int(row["stock"]),
        )
        context.product_db.append(product)


@given('a product exists with name "{name}" and price "{price}"')
def step_load_single_product(context, name, price):
    """Load a single product with name and price into the system."""
    if not hasattr(context, "product_db"):
        context.product_db = []
    product = make_product(name=name, price=float(price))
    context.product_db.append(product)


@given('the product catalog is empty')
def step_empty_product_catalog(context):
    """Ensure the product catalog starts empty."""
    context.product_db = []


@given('there are "{count:d}" products in the system')
def step_load_multiple_products(context, count):
    """Load a specific number of fake products into the system."""
    context.product_db = [make_product() for _ in range(count)]


@given('the system is ready')
def step_system_ready(context):
    """Initialize the system state before each scenario."""
    context.product_db = []
    context.results = []
    context.response_message = None
