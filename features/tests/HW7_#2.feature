# Created by babao at 3/25/2023
Feature: Add a product to cart
  Scenario: Add a product to cart from search results
    Given Open Amazon B09Y939KR2 page
    When Click Add to Cart
    Then Verify cart count is increased by 1


  Scenario: search for piano stand
    Given Open Amazon page
    When Input text piano stand
    When Click on search icon
    When Click on the first product
    When Click Add to Cart
    Then Verify cart count is increased by 1