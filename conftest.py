import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en",
        help="Choose browser language, e.g. en, es, fr"
    )

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )
    print(f"\nLaunching Chrome with language: {user_language}")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nClosing browser...")
    browser.quit()