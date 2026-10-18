
from behave import given, when, then
from src.features.pages.base_page import BasePage


@given(u'the user opens the website')
def step_open_site(context):
    base_page = BasePage(context.page)
    context.base_page = base_page
    base_page.navigate_to_web()

@when(u'catalog page has loaded')
def step_catalog_load(context):
    context.base_page.initial_heading.is_visible


@then(u'the "Läslisten" headline should be displayed')
def step_display_headline(context):
    context.base_page.initial_heading.is_visible()


@then(u'the "Välkommen!" text should be displayed')
def step_display_welcome(context):
    context.base_page.welcome_heading.is_visible()

