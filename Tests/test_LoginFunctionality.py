import time

import pytest
from playwright.sync_api import expect
from playwright.sync_api import Playwright

from PageObject.DashboardPage import DashboardPage
from PageObject.LoginPage import LoginPage
from PageObject.PasswordNewPage import PasswordNewPage
from PageObject.RegisterPage import RegisterPage
from PageObject.commonElements import CommonElements
from TestData.LoginTestData import LoginTestData


@pytest.fixture(params=LoginTestData.validCredentials)
def getData(request):
    return request.param

def test_validLogin(invoke_Browser, getData):
    loginPage = LoginPage(invoke_Browser)
    loginPage.navigate_to_url()
    dashboardPage = loginPage.do_logIn(getData["email"], getData["password"])
    dashboardPage.verify_homebutton_appHeader()

@pytest.fixture(params=LoginTestData.invalidPassword)
def getWrongData(request):
    return request.param

def test_wrongPassword(invoke_Browser, getWrongData):
    loginPage = LoginPage(invoke_Browser)
    loginPage.navigate_to_url()
    loginPage.do_logIn(getWrongData["email"], getWrongData["password"])
    common_element = CommonElements(invoke_Browser)
    expect(common_element.getToastMessage()).to_be_visible()
    print(common_element.getToastMessage().text_content())
    expect(common_element.getToastMessage()).to_have_text("Incorrect email or password.")


def test_empty_emailAndPassword(invoke_Browser):
    loginPage = LoginPage(invoke_Browser)
    loginPage.navigate_to_url()
    loginPage.do_logIn("", "")
    expect(loginPage.getEmailRequired()).to_be_visible()
    print(loginPage.getEmailRequired().text_content())
    expect(loginPage.getPasswordRequired()).to_be_visible()
    print(loginPage.getPasswordRequired().text_content())

def test_RegisterButton_LoginHere_RegisterHere_Link(invoke_Browser):
    loginPage = LoginPage(invoke_Browser)
    loginPage.navigate_to_url()
    loginPage.getRegisterBtn().click()
    time.sleep(2)
    loginPage.getLoginHereLink().click()
    time.sleep(2)
    loginPage.getRegisterHereLink().click()
    time.sleep(2)

@pytest.fixture(params=LoginTestData.passwordReset)
def getPasswordResetData(request):
    return request.param

def test_forgotPassword_reset_new_password(invoke_Browser, getPasswordResetData):
    loginpage = LoginPage(invoke_Browser)
    loginpage.navigate_to_url()
    loginpage.getForgotPassword().click()
    passwordnewpage = PasswordNewPage(invoke_Browser)
    passwordnewpage.do_Save_new_Password(getPasswordResetData["email"], getPasswordResetData["password"], getPasswordResetData["confirmpassword"])
    commonelements = CommonElements(invoke_Browser)
    expect(commonelements.getToastMessage()).to_be_visible()
    expect(commonelements.getToastMessage()).to_have_text("Password Changed Successfully")


@pytest.fixture(params=LoginTestData.registerData)
def getResiterData(request):
    return request.param

def test_registerBtn_register_user_already_existing(invoke_Browser, getResiterData):
    loginPage = LoginPage(invoke_Browser)
    loginPage.navigate_to_url()
    loginPage.getRegisterBtn().click()
    registerPage = RegisterPage(invoke_Browser)
    registerPage.do_register(getResiterData["FirstName"], getResiterData["LastName"], getResiterData["Email"], getResiterData["Phone_No"], getResiterData["Occupation"], getResiterData["Gender"], getResiterData["Password"], getResiterData["ConfirmPassword"])
    commonElements = CommonElements(invoke_Browser)
    expect(commonElements.getToastMessage()).to_be_visible()
    expect(commonElements.getToastMessage()).to_contain_text("User already exisits with this Email Id!")