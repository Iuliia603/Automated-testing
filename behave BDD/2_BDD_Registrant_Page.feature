Feature: Registrant functionality


  Background:
    Given a web browser is open
    And user is at the Brainbucket registrant page


  Scenario: Registration with Required Fields

    Given all fields are cleared
    When user enters all required fields
    And user clicks Submit button
    Then user's account has been created


  Scenario: Registration without Required Fields

    Given all fields are cleared
    When user clicks Submit button
    Then warning shown about 'You must agree to the Privacy Policy!'
