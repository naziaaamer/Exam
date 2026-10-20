
from behave import given, when, then
from playwright.sync_api import expect
from src.features.pages.add_book import AddBook


@given(u'the user is on the start page')
def step_impl(context):
    add_book = AddBook(context.page)
    context.add_book = add_book
    add_book.navigate()


@when(u'the user click on "Lägg till bok" button')
def step_impl(context):
    context.add_book.add_book_button.click()


@when(u'the user enters book Title "if tomorrow comes"')
def step_impl(context):
    context.add_book.book_name.fill("if tomorrow comes")


@when(u'the user enters Förfatare "sidney sheldon"')
def step_impl(context):
    context.add_book.author_name.fill("sidney sheldon")


@when(u'the user clicks on "Lägg till ny bok" button')
def step_impl(context):
    context.add_book.add_new_book.click()


@then(u'the book name "if tomorrow comes" should display on Katalog page')
def step_impl(context):
    context.add_book.katalog_button.click()
    expect(context.add_book.book_title).to_be_visible()