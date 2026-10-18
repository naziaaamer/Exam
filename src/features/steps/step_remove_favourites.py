

from behave.api.pending_step import StepNotImplementedError
from behave import given, when, then


@when(u'the user click on heart icon')
def step_impl(context):
    context.page.get_by_test_id("star-Python för folk som hatar ormar").click()

@then(u'the heart icon is not visible as highlighted')
def step_impl(context):
    raise StepNotImplementedError(u'Then the heart icon is not visible as highlighted')


@when(u'the user click on Mina böcker')
def step_impl(context):
    raise StepNotImplementedError(u'When the user click on Mina böcker')


@then(u'the book is not displayed under favourites')
def step_impl(context):
    raise StepNotImplementedError(u'Then the book is not displayed under favourites')