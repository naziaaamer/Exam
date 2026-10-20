from behave import given, when, then
from playwright.sync_api import expect

from src.features.pages.add_to_favourites import AddFavourites
from src.features.pages.base_page import BasePage


@when(u'the user clicks on heart icon')
def step_impl(context):
    base_page = BasePage(context.page)
    context.base_page = base_page
    context.base_page.favourites_button.click()

@then(u'the heart icon should be displayed on screen')
def step_impl(context):
    expect(context.base_page.favourites_icon).to_be_visible()

@when(u'the user clicks on Mina böcker button')
def step_impl(context):
    context.base_page.mina_booker_button.click()


@then(u'the book should be displayed under Mina böcker tab')
def step_impl(context):
    add_fav = AddFavourites(context.page)
    context.add_fav = add_fav
    expect(context.add_fav.book_name).to_be_visible()