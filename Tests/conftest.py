import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Data.login_data import login
from PagesObjects.HomePage import HomePage
from PagesObjects.LoginPage import LoginPage


@pytest.fixture(scope='function')
def setup():
    options = Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get('https://demowebshop.tricentis.com/')


    yield driver
    driver.quit()

@pytest.fixture
def home_page(setup):
    return HomePage(setup)

@pytest.fixture
def login_page(setup):
    return LoginPage(setup)

@pytest.fixture
def formulaire_enregistrement():
    return login.fill_register_form()

@pytest.fixture
def formulaire_enregistrement_echoue():
    return login.fill_register_form_avec_credentials_existant()