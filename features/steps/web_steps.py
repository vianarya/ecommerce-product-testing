from behave import given, when, then


# ─────────────────────────────────────────────
# BUTTON CLICK STEP DEFINITIONS
# ─────────────────────────────────────────────

@when('I press the "{button_name}" button')
def step_press_button(context, button_name):
    """Step definition for clicking a button by its name."""
    button = context.driver.find_element_by_xpath(
        f'//button[contains(text(), "{button_name}")]'
    )
    button.click()


@when('I click the "{button_name}" button')
def step_click_button(context, button_name):
    """Alternative step for clicking a button."""
    button = context.driver.find_element_by_xpath(
        f'//button[contains(text(), "{button_name}")]'
    )
    button.click()


# ─────────────────────────────────────────────
# GIVEN STEP DEFINITIONS
# ─────────────────────────────────────────────

@given('there are products available in the system')
def step_products_available(context):
    """Ensure products exist in the system."""
    assert len(context.product_db) > 0, "No products found in the system"


@given('the product catalog is empty')
def step_empty_catalog(context):
    """Clear all products from the system."""
    context.product_db.clear()


@given('the following products exist in the system')
def step_products_exist(context):
    """Load products from the feature table into the system."""
    context.product_db = []
    for row in context.table:
        context.product_db.append({
            "name": row["name"],
            "price": float(row["price"]),
            "category": row["category"],
            "stock": int(row["stock"]),
        })


# ─────────────────────────────────────────────
# THEN STEP DEFINITIONS
# ─────────────────────────────────────────────

@then('I should receive a "{message}" message')
def step_check_message(context, message):
    """Check that the expected message is returned."""
    assert context.response_message == message, (
        f"Expected '{message}' but got '{context.response_message}'"
    )


@then('I should see the following products in the results')
def step_check_products_in_results(context):
    """Check that all expected products appear in the results."""
    result_names = [p["name"] for p in context.results]
    for row in context.table:
        assert row["name"] in result_names, (
            f"Product '{row['name']}' not found in results"
        )


@then('the results should contain at least {count:d} products')
def step_check_result_count(context, count):
    """Check that results contain at least the expected number of products."""
    assert len(context.results) >= count, (
        f"Expected at least {count} products, got {len(context.results)}"
    )


@then('the results should be empty')
def step_check_empty_results(context):
    """Check that the results list is empty."""
    assert len(context.results) == 0, (
        f"Expected empty results but got {len(context.results)} products"
    )
