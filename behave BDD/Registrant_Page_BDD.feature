Feature: Registrant functionality
  Background:
    Given User launch refistrant page

  Scenario: User fills in all required fields
    Given All fields are cleared
    When User enters all required fields
    And User clicks Submit button
    Then User's account has been created

  Scenario: User leaves the required fields empty
    Given All fields are cleared
    When User clicks Submit button
    Then Warning will be shown about 'You must agree to the Privacy Policy!'
    