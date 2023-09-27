Feature: Show available products


  Background:
    Given a web browser is open
    And user is at the Brainbucket home page


  Scenario: Show all available Desktops

    Given no products are selected
    When user selects 'Show all Desktops' from Product Menu
    Then the available Desktops are displayed


  Scenario: Show available PC products

    Given no products are selected
    When user selects PC Desktops from Product Menu
    Then the available PC Desktops are displayed


  Scenario: Show available Mac products

    Given no products are selected
    When user selects Mac Desktops from Product Menu
    Then the available Mac Desktops are displayed