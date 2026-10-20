#noinspection CucumberUndefinedStep
Feature: view catalog
  # use story
  # As a user,
  # I want to access the website and see the Katalog
  # so that I can look at the available books.

  Scenario: open website and view catalog

    Given the user is on start page
    When catalog page has loaded
    Then the "Läslisten" headline should be displayed
    And the "Välkommen!" text should be displayed

