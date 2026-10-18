#noinspection CucumberUndefinedStep
Feature: add new book to catalog
  # As a user,
  # I want to add new books on Katalog using "Lägg till bok" by entering the required information,
  # so that newly added books appear in the Katalog.

  Scenario: navigate to website and add book to catalog
    Given the user is on the start page
    When the user click on "Lägg till bok" button
    And the user enters book Title "if tomorrow comes"
    And the user enters Förfatare "sidney sheldon"
    And the user clicks on "Lägg till ny bok" button
    Then the book name "if tomorrow comes" should display on Katalog page
