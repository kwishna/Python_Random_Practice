Feature: This Is a Sample Feature

  Scenario: First Scenario
    Given I am creating a feature file
    Then I will create step file
    Then I will create a runner file

  Scenario Outline: First Scenario
    Given I am creating a <first name> file
    Then I will create a <middle name> step file
    Then I will create a <last name> runner file
    Examples:
      | first name | middle name | last name |
      | krishna | kumar | singh |
      | singh  | kumar  | krishna |