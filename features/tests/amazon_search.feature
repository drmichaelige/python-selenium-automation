# Created by babao at 3/11/2023
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Amazon page
    When Input {search_word} into search field
    Then Click on search icon
    Then Product results for {search_word}  are shown
