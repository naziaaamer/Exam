from behave import when, then
from playwright.sync_api import expect

from src.features.pages.add_to_favourites import AddFavourites


@when(u'the user click on heart icon again')
def fav_buttons_click(context):
    context.base_page.favourites_button.click()


@then(u'the heart icon is not visible as highlighted')
def fav_button_disabled(context):
    expect(context.base_page.favourites_button).not_to_have_class("star selected")


@when(u'the user click on Mina böcker')
def my_books(context):
    context.base_page.mina_booker_button.click()


@then(u'the book is not displayed under favourites')
def books_not_on_my_books(context):
    add_fav = AddFavourites(context.page)
    context.add_fav = add_fav
    expect(context.add_fav.book_name).not_to_be_visible()
