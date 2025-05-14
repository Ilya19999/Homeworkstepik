import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en", help="Choose language: en, fr, es, etc."
    )

@pytest.fixture(scope="function")
def language(request):
    return request.config.getoption("language")
