from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By
from pages.SearchPage import SearchPage

@given('I navigate to the google page')
def step_impl(context):
    global searchPage
    searchPage = SearchPage(context)
    context.driver.get(context.user_configs['base_url'])
    assert_that(context.driver.title, equal_to("Google"))

@step('I search for "{search_term}"')
def step_impl(context, search_term):
    searchPage.search_term(search_term)

@step('I see a search result containing "{search_result}"')
def step_impl(context, search_result):
    text = searchPage.get_element_matching_text(search_result).text
    assert_that(search_result in text)
