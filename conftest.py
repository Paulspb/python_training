
import pytest
import json
import os.path
import importlib
    #less 6.6
import jsonpickle
from fixture.application import Application

fixture = None
    #less 6.1
    # remember for working directory. before lesson 6.1 it not be empty
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
        # access to pytest_addoption(parser):
    browser = request.config.getoption("--browser")
    if target is None:
            # less 6.2
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
            # -del less 6.2 with open(request.config.getoption("--target")) as config_file:
            #with open(config_file) as config_file:
        with open(config_file) as f:
            target = json.load(f)
            # revoked less 6.1 delete base_url = request.config.getoption("--baseUrl")
            # lesson 5,5  using hook - зацепка - из описаний pyton
    if fixture is None or not fixture.is_valid():
            # on less 6.1fixture = Application(browser=browser,base_url=base_url)
        fixture = Application(browser=browser)
                # less 6.1 fixture = Application(browser=browser, base_url=target['baseUrl'])
                #fixture.session.ensure_login(username="admin", password="secret")
    fixture.session.ensure_login(username=target['username'], password=target['password'])
        # less 6.1
    return fixture

@pytest.fixture(scope = "session", autouse= True)
def stop(request):
        # stop not defined anuthere
    def fin():
        # less 6.1
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
        # less 6.1
    return fixture

# lesson 5.5 from cmd line
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
        # less 6.1
        #parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--target", action="store", default="target.json")

# less 6.5
def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        # for fixture with prefix -data_ -
        if fixture.startswith("data_"):
                    # def test_add_group(app, data_groups):
                    # here data loading from data/groups.json
            testdata = load_from_module(fixture[5:])
            # it need to paramatrise our test function
                                            # for bnest interpretation fo data
                                            #ids=[str(x) for x in testdata])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

        elif fixture.startswith("json_"):
        #-revoke- less 6.6 elif fixture.startswith("data_"):
                    # here data loading from data/groups.json
            testdata = load_from_json(fixture[5:])
            # it need to paramatrise our test function
                                            # for bnest interpretation fo data
                                            #ids=[str(x) for x in testdata])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
        # here data loading from data/groups.json
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
        # here data loading from data/groups.json
        # how  to tell the prog : take input from Group or contact ? take  one lib called
        # jsonpickle with option : jsonpickle.set_encoder_options("json", indent=2)
        # then load result file __file_ + data/groups.json
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())


    #pickle.dump()

    #return importlib.import_module("data.%s" % module).testdata
