Feature: Login

    Scenario Outline:  Insert an incorrect name
        Given I am on the login page
        When I set "<name>" as name
        And I press the login button
        Then I see a message that says "<msg>"
        Examples: LoginNames
            | name                         | msg                                                       |
            | con espacios                 | El nombre no puede tener caracteres especiales o espacios |
            | holamellamoagustinetcheverry | El nombre no debe tener mas de 25 caracteres              |
            | xd                           | El nombre debe tener mas de 2 caracteres                  |
            | @3hola                       | El nombre no puede tener caracteres especiales o espacios |

    Scenario: Insert a name correctly
        Given I am on the login page
        When I set Agustin as name
        And I press the login button
        Then Start the game