from behave import given, when, then
from playwright.sync_api import expect

from src.features.pages.add_to_favourites import AddFavourites


@when(u'the user click on heart icon again')
def step_impl(context):
    context.base_page.favourites_button.click()


@then(u'the heart icon is not visible as highlighted')
def step_impl(context):
    expect(context.base_page.favourites_button).not_to_have_class("star selected")


@when(u'the user click on Mina böcker')
def step_impl(context):
    context.base_page.mina_booker_button.click()


@then(u'the book is not displayed under favourites')
def step_impl(context):
    add_fav = AddFavourites(context.page)
    context.add_fav = add_fav
    expect(context.add_fav.book_name).not_to_be_visible()