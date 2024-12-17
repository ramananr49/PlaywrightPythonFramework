from playwright.sync_api import expect


class PasswordNewPage():

    def __init__(self, page):
        self.page = page
        self._enterNewPasswordHeader = page.locator("h3.card-title")
        self._emailTextbox = page.locator("input[formcontrolname='userEmail']")
        self._passwordTextbox = page.locator("input[id='userPassword']")
        self._confirmPassword = page.locator("input[id='confirmPassword']")
        self._saveNewPasswordButton = page.locator("button[type='submit']")
        self._loginLink = page.locator("//a[text()='Login']")
        self._registerLink = page.locator("//a[text()='Register']")


    def getEnterNewPasswordHeader(self):
        return self._enterNewPasswordHeader

    def getEmailTextbox(self):
        return self._emailTextbox

    def getPasswordTextbox(self):
        return self._passwordTextbox

    def getConfirmPassword(self):
        return self._confirmPassword

    def getSaveNewPassword(self):
        return self._saveNewPasswordButton

    def getLoginLink(self):
        return self._loginLink

    def getRegisterLink(self):
        return self._registerLink

    def do_Save_new_Password(self, email, password, confirmpassword):
        expect(self.getEnterNewPasswordHeader()).to_contain_text("Enter New Password")
        self.getEmailTextbox().fill(email)
        self.getPasswordTextbox().fill(password)
        self.getConfirmPassword().fill(confirmpassword)
        self.getSaveNewPassword().click()