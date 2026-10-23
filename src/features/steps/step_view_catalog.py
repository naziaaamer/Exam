
from behave import given, when, then
from playwright.sync_api import expect
from src.features.pages.base_page import BasePage


@given(u'the user is on start page')
def step_open_site(context):
    base_page = BasePage(context.page)
    context.base_page = base_page
    base_page.navigate_to_web()


@when(u'catalog page has loaded')
def step_catalog_load(context):
    expect(context.base_page.initial_heading).to_be_visible()


@then(u'the "Läslisten" headline should be displayed')
def step_display_headline(context):
    expect(context.base_page.initial_heading).to_be_visible()


@then(u'the "Välkommen!" text should be displayed')
def step_display_welcome(context):
    expect(context.base_page.welcome_heading).to_be_visible()
