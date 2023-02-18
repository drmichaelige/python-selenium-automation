# Created by babao at 2/17/2023
Feature: Amazon Cart Empty tests

  Scenario: User verifies the cart is empty
    Given Open Amazon page
    When Click Cart icon
    Then Cart page opens
    Then Verify "Your Amazon Cart is Empty" is displayed


