# Created by babao at 3/10/2023
Feature: Test Scenarios to verify Amazon results

Scenario: User verify product image and name in search results
    Given Open Amazon page
    When  Input wallet results into search field
    Then Click on search icon
    Then Verify all results have product image and name
