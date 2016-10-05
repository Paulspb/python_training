import pytest
import json
import os.path
import importlib
    #less 6.6
import jsonpickle
from fixture.application import Application
    # less 7.1
from fixture.db import DbFixture

fixture = None
    #less 6.1
    # remember for working directory. before lesson 6.1 it not be empty
target = None

#---- less 7.1 now there is two fixture, it needs to load only one from these two
def load_config(file):
    global target
        #- means target.json has not loaded
    if target is None:
            # less 6.2
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
            # -del less 6.2 with open(request.config.getoption("--target")) as config_file:
            #with open(config_file) as config_file:
        with open(config_file) as f:
            target = json.load(f)
            # revoked less 6.1 delete base_url = request.config.getoption("--baseUrl")
            # lesson 5,5  using hook - зацепка - из описаний pyton
    return target

@pytest.fixture
#-------------------- fixture #1 ------------
def app(request):
    global fixture
    # revoke  less 7.1 global target
        # access to pytest_addoption(parser) via app(request):
        # less 5.5:
    browser  = request.config.getoption("--browser")
    # -revoke- less 7.2:     base_url = request.config.getoption("--baseUrl")
        # less 7.1  take from target.json ONLY block -web-
    web_config = load_config(request.config.getoption("--target"))['web']
    # less 7.1 if target is None:
            # less 6.2
        # less 7.1 config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
            # -del less 6.2 with open(request.config.getoption("--target")) as config_file:
            #with open(config_file) as config_file:
        # less 7.1 with open(config_file) as f:
        # less 7.1     target = json.load(f)
            # revoked less 6.1 delete base_url = request.config.getoption("--baseUrl")
            # lesson 5,5  using hook - зацепка - из описаний pyton
    if fixture is None or not fixture.is_valid():
            # on less 6.1fixture = Application(browser=browser,base_url=base_url)
            # access to pytest_addoption(parser):
            # less 5.5:
        #browser  = request.config.getoption("--browser")
        #base_url = request.config.getoption("--baseUrl")
            # less 5.5 fixture = Application(browser=browser)
        # less 7.1         fixture = Application(browser=browser, base_url=base_url)
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
                # less 6.1 fixture = Application(browser=browser, base_url=target['baseUrl'])
                #fixture.session.ensure_login(username="admin", password="secret")
    #less 7.1 fixture.session.ensure_login(username=target['username'], password=target['password'])
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
        # less 6.1
    return fixture
#------------------------- less 7.1 DB
    # add something for DB connect
    # scope = "session" ---- for init at the begon of session and stop at hte end (ones only)
@pytest.fixture(scope = "session")
def db(request):
        # read from target.json , part -db-
    db_config = load_config(request.config.getoption("--target"))['db']
        # this is new class - DbFixture into packge -fixture-
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'] )
        # new class
    def fin():
        dbfixture.destroy()
    # do registration of request
    request.addfinalizer(fin)
    return dbfixture

#-------------------- fixture #2 ----------------------------------------
@pytest.fixture(scope = "session", autouse= True)
    # read data from -target.json-
def stop(request):
        # stop not defined anuthere
    def fin():
        # less 6.1 + 7.2
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
        # less 6.1
    return fixture

# lesson 5.5 from cmd line . it add parameters from cmd line. it access from def app(request)
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
