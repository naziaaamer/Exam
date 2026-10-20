#noinspection CucumberUndefinedStep
Feature: add books to favourites
  # As a user,
  # I want to add books in "Mina böcker",
  # so that I can keep track of my favourite books.

    Scenario: navigate to website and add book to favourites from catalog
      Given the user is on start page
      When the user clicks on heart icon
      Then the heart icon should be displayed on screen
      When the user clicks on Mina böcker button
      Then the book should be displayed under Mina böcker tab


