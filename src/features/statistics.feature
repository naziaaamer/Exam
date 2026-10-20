#noinspection CucumberUndefinedStep
Feature: user can view statistics
  # User story
  # As a user,
  # I want to see the Statistik showing total number of books and favourites,
  # so that I can keep track of my favourites and Katalog.

  Scenario: navigate to website and user can click on statistics button and view statistics
    Given the user is on the start page
    When the user clicks on Statistisk button
    Then the user is navigated to statistics screen and can view headline as "Välkommen!"
    And the user can view total number of books
    And the user can view total number of books added as favourites