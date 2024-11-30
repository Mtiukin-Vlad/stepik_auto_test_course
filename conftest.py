import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, hu")

@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("--language")
    yield language