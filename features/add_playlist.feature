Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Add just playlist name
    Given I login as user "user" with password "password"
    When I add playlist
      | name        |
      | Temazos     |
    Then I'm viewing the details page for playlist by "user"
      | name        |
      | Temazos     |
    And There are 1 playlist