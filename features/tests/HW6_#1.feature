# Created by babao at 3/12/2023
Feature: Test Scenarios on Amazon Privacy Notice

Scenario: User can open and close Amazon Privacy Notice
 Given Open Amazon page
 Given Open Conditions of Use page
 And Store original windows
 And Click on Amazon Privacy Notice link
 When Switch to new window
 Then Verify Amazon Privacy Notice page is opened
 And Close page switch back to original
