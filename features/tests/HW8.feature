# Created by babao at 3/27/2023
Feature: User can check some actions

Scenario: User can search and select in a department
Given Open Amazon page
When Select Baby department
When Input text teething toys
And Click on search icon
Then Verify Baby store is selected


Scenario: User hovers over Arrivals
Given Open Amazon B074TBCSC8 page
When Hover over New Arrivals
Then Verify user sees the details