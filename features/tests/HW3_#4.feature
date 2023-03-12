# Created by babao at 2/18/2023
Feature: Test Scenarios to add product to cart

  Scenario: User verifies product is added to cart
    Given Open Amazon page
    When Input text 48 Laws
    Then Click on search icon
    And Click on product
    And Click add to cart
    Then Confirm cart count for 48 Laws
