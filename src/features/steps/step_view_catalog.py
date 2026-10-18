
from behave import given, when, then


@given(u'the user opens the website')
def step_open_site(context):
    context.page.goto(context.base_url, timeout=15000)


@when(u'catalog page has loaded')
def step_catalog_load(context):
    context.page.get_by_role("heading", name=" Läslistan ").wait_for()


@then(u'the "Läslisten" headline should be displayed')
def step_display_headline(context):
    context.page.get_by_role("heading", name=" Läslistan ").is_visible()


@then(u'the "Välkommen!" text should be displayed')
def step_display_welcome(context):
    context.page.get_by_role("heading", name=" Välkommen!").is_visible()

