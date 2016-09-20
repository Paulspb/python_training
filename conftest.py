
import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        # access to pytest_addoption(parser):
        browser =  request.config.getoption("--browser")
        # lesson 5,5  using hook - зацепка - из описаний pyton
        fixture = Application(browser=browser)
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope = "session", autouse= True)
def stop(request):
    # stop not defined anuthere
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)

# lesson 5.5 from cmd line
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
