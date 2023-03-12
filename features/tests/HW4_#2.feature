# Created by babao at 2/20/2023
Feature: Test Scenarios to add any product to cart

Scenario: User verifies any product is added to cart
    Given Open Amazon page
    When Input text shower curtain
    Then Click on search icon
    Then Click select product
    And Store the product name
    And Click add to cart
    Then Verify cart count for  shower curtain
