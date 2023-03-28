# Created by babao at 3/24/2023
Feature: Page Object patterns

Scenario: Logged out user sees Sign in page when clicking Orders
Given Open Amazon page
When  Click Amazon Orders link
Then  Verify Sign In page is opened


Scenario: Verify 'Your Shopping Cart is empty' shown if no product added
Given Open Amazon page
When  Click on cart icon
Then  Verify Your Shopping Cart is empty text present
