#@negative
# Scenario: User can't login without entering password
#  Given user is not logged in
#  When user enters email
#  And user clicks Login button
#  Then warning is shown No match for E-Mail Address and/or Password
#
#@negative @skip
#Scenario: User can't login without entering email
#  Given user is not logged in
#  When user enters password
#  And user clicks Login button
#  Then warning is shown No match for E-Mail Address and/or Password

Feature: Login functionality is negative

  @negative
Scenario Outline: User can't login without entering <field>
  Given user is not logged in
  When user enters "<value>" in "<field>"
  And user clicks Login button
  Then warning is shown No match for E-Mail Address and/or Password

  Examples:
    | field    | value |
    | email    | None  |
    | password | None  |