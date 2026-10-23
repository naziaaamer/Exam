from behave import when, then
from playwright.sync_api import expect
from src.features.pages.view_statistics import Statistics


@when(u'the user clicks on Statistisk button')
def statistics_button(context):
    view_stats = Statistics(context.page)
    context.view_stats = view_stats

    context.view_stats.statistics_button.click()


@then(u'the user is navigated to statistics screen and can view headline as "Välkommen!"')
def statistics_screen(context):
    expect(context.view_stats.welcome_heading).to_be_visible()


@then(u'the user can view total number of books')
def books_number(context):
    expect(context.view_stats.books_count).to_be_visible()


@then(u'the user can view total number of books added as favourites')
def books_marked_favorites(context):
    expect(context.view_stats.favourites_count).to_be_visible()
