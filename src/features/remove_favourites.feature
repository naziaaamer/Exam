#noinspection CucumberUndefinedStep
Feature: remove books from favourites
  # As a user,
  # I want to remove books from "Mina böcker",
  # so that I can manage my favourites.

      Scenario: navigate to website and remove book from favourites
        Given the user is on start page
        When the user mouse hover on heart icon before book name
        And the user clicks on heart icon
        Then the heart icon should be displayed on screen
        When the user click on heart icon
        Then the heart icon is not visible as highlighted
        When the user click on Mina böcker
        Then the book is not displayed under favourites
