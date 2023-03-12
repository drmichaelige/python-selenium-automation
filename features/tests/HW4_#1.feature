# Created by babao at 2/20/2023
Feature: Test Scenarios to count Amazon Best Sellers links

Scenario: User counts Amazon bestseller links
    Given Open BestSellers page
    Then Verify Bestsellers menu links present
    Then Verify Bestsellers has 5 links
