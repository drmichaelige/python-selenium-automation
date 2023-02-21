# Created by babao at 2/20/2023
Feature: Test Scenarios to add any product to cart

Scenario: User verifies any product is added to cart
    Given Open Amazon page
    When Input text shower curtain
    And Click the search icon
    And Click select product
    And Click add to cart
    Then Verify cart count for  shower curtain
