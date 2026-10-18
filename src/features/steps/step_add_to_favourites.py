from behave import given, when, then
from src.features.pages.add_to_favourites import AddFavourites


@given(u'the user is on start page')
def step_impl(context):
    add_fav = AddFavourites(context.page)
    context.add_fav = add_fav
    add_fav.navigate()


@when(u'the user mouse hover on heart icon before book name')
def step_impl(context):
    context.add_fav.hover_favourites.hover()


@when(u'the user clicks on heart icon')
def step_impl(context):
    context.add_fav.favourites_button.click()


@then(u'the heart icon should be displayed on screen')
def step_impl(context):
    context.add_fav.favourites_button_visible.is_visible()


@when(u'the user clicks on Mina böcker button')
def step_impl(context):
    context.add_fav.mina_bocker_button.click()


@then(u'the book should be displayed under Mina böcker tab')
def step_impl(context):
    context.add_fav.book_name.is_visible()