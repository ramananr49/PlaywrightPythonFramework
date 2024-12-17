from PageObject.DashboardPage import DashboardPage


class LoginPage():

    def __init__(self, page):
        self.page = page
        self._emailTextbox = page.locator("#userEmail")
        self._passwordTextbox = page.locator("#userPassword")
        self._loginButton = page.locator("#login")
        self._forgotPassword = page.get_by_role("link", name="Forgot password?")
        self._emailRequired = page.locator("//label[text()='Email']/following-sibling::div")
        self._passwordRequired = page.locator("//label[text()='Password']/following-sibling::div")
        self._registerButton = page.get_by_role("link", name="Register")
        self._LoginHereLink = page.locator("//a[text()='Login here']")
        self._RegisterHereLink = page.locator("//a[text()='Register here']")

    def getEmailTxtBox(self):
        return self._emailTextbox

    def getPasswordTxtBox(self):
        return self._passwordTextbox

    def getLoginBtn(self):
        return self._loginButton

    def getForgotPassword(self):
        return self._forgotPassword

    def getEmailRequired(self):
        return self._emailRequired

    def getPasswordRequired(self):
        return self._passwordRequired

    def getRegisterBtn(self):
        return self._registerButton

    def getLoginHereLink(self):
        return self._LoginHereLink

    def getRegisterHereLink(self):
        return self._RegisterHereLink

    def navigate_to_url(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def do_logIn(self, email, password):
        self.getEmailTxtBox().fill(email)
        self.getPasswordTxtBox().fill(password)
        self.getLoginBtn().click()
        dashboardPage = DashboardPage(self.page)
        return dashboardPage