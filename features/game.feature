Feature: Play a game

    Scenario: Win a game
        Given I set giova as name
        And Start a game
        When Insert correct letters
        Then I see a message that says Ganaste

    Scenario: Lose a game
        Given I set eche as name
        And Start a game
        When Insert six wrong letters
        Then I see a message that says Perdiste
