Feature: Login functionality


  Background:
    Given user launch login page


  Scenario: Log in with the correct Email and Password

    Given user is not logged in
    When user enters correct Email and Password
    And user clicks Login button
    Then user's profile is launched


  Scenario: Login without entering a Email and Password

    Given user is not logged in
    When user clicks Login button
    Then warning shown about 'No match for E-Mail Address and/or Password'


  Scenario: Login without entering a Password

    Given user is not logged in
    When user enters correct Email
    And user clicks Login button
    Then warning shown about 'No match for E-Mail Address and/or Password'


  Scenario: Log in with the incorrect Password

    Given user is not logged in
    When user enters correct Email and incorrect Password
    And user clicks Login button
    Then warning shown about 'No match for E-Mail Address and/or Password'


  Scenario: Log in with the incorrect Email

    Given user is not logged in
    When user enters incorrect Email and correct Password
    And user clicks Login button
    Then warning shown about 'No match for E-Mail Address and/or Password'


