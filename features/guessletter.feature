Feature: Guess letter

  Scenario: Guess a letter correctly
    Given I set damian as name
    And Start a game
    When Insert letter a
    And Try letter
    Then Letter shows in word

  Scenario: Guess a letter incorrectly
    Given I set damian as name
    And Start a game
    When Insert letter x
    And Try letter
    Then Letter shows in incorrect array