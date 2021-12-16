Feature: Guess letter

  Scenario: Guess a letter correctly
    Given I set damian as name
    And Start a game
    And Insert letter
    And Try letter
    When Letter is correct
    Then Letter shows in word

  Scenario: Guess a letter incorrectly
    Given I set damian as name
    And Start a game
    And Insert letter
    And Try letter
    When Letter is incorrect
    Then Letter shows in incorrect array