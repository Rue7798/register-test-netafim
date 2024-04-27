Feature: Registration

  Scenario: register new user
    Given the user is on the homepage
    When the user clicks on the "Signup / Login" button
    Then the "New User Signup!" is displayed
    When the user enters their name and email address
    when clicks the "Signup" button
    Then the "ENTER ACCOUNT INFORMATION" page is displayed
    When the user fills in the account information
    when user selects the checkboxes
    when user fills in the personal information
    when user clicks the "Create Account" button
    Then the "ACCOUNT CREATED!" message is visible
    When the user clicks the "Continue" button
    Then the "Logged in as username" is visible
    When the user clicks the "Delete Account" button
    Then the "ACCOUNT DELETED!" message is displayed
    Then the user clicks the "Continue" button