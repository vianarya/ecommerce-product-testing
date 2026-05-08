Feature: Product Management
  As a user of the e-commerce platform
  I want to manage products
  So that I can view, search, and interact with the product catalog

  Background:
    Given the following products exist in the system:
      | name    | price | category  | stock |
      | Hat     | 15.00 | Clothing  | 50    |
      | Shoes   | 59.99 | Clothing  | 30    |
      | Big Mac | 5.99  | Food      | 100   |
      | Sheets  | 25.00 | Home      | 20    |

  # ─────────────────────────────────────────────
  # LISTING ALL PRODUCTS SCENARIO
  # ─────────────────────────────────────────────

  Scenario: Successfully list all products
    Given there are products available in the system
    When I press the "Clear" button to remove previous entries
    And I press the "Search" button
    Then I should receive a "Success" message
    And I should see the following products in the results:
      | name    |
      | Hat     |
      | Shoes   |
      | Big Mac |
      | Sheets  |

  Scenario: List all products returns correct count
    When I press the "Clear" button to remove previous entries
    And I press the "Search" button
    Then I should receive a "Success" message
    And the results should contain at least 4 products

  Scenario: List all products when no products exist
    Given the product catalog is empty
    When I press the "Clear" button to remove previous entries
    And I press the "Search" button
    Then I should receive a "Success" message
    And the results should be empty
