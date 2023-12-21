Feature: Functionality Youtube video

  Background:
    Given user opens website youtube.com
    And user Enter search request in the input field

  Scenario:
    When find in results video name
    And user clicks on the video
    Then video started to play after opening
    When user clicks on 1/3
    Then the video continues to play