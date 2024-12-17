from playwright.sync_api import expect, Page


class RegisterPage():


    def __init__(self, page: Page):
        self.page = page
        self._registerHeader = page.locator("h1.login-title")
        self._firstName = page.locator("input#firstName")
        self._lastName = page.locator("input#lastName")
        self._email = page.locator("input#userEmail")
        self._phoneNumber = page.locator("input#userMobile")
        self._occupation = page.locator("select[formcontrolname='occupation']")
        self._genderMale = page.locator("input[value='Male']")
        self._genderFemale = page.locator("input[value='Female']")
        self._password = page.locator("input#userPassword")
        self._confirmPassword = page.locator("input#confirmPassword")
        self._iAm18YearOrOlder = page.locator("input[formcontrolname='required']")
        self._registerButton = page.locator("input#login")

    def getRegisterHeader(self):
        return self._registerHeader

    def getFirstNameTextbox(self):
        return self._firstName

    def getLastNameTextbox(self):
        return self._lastName

    def getEmailTextbox(self):
        return self._email

    def getPhoneNumber(self):
        return self._phoneNumber

    def getOccupationDropdown(self):
        return self._occupation

    def getGenderMale(self):
        return self._genderMale

    def getGenderFemale(self):
        return self._genderFemale

    def getPassword(self):
        return self._password

    def getConfirmPassword(self):
        return self._confirmPassword

    def getIAm18YearsOrOlderCheckbox(self):
        return self._iAm18YearOrOlder

    def getRegisterButton(self):
        return self._registerButton

    def do_register(self, fName, LName, email, Phone_no, Occupation, gender, password, confirmpassword):
        expect(self.getRegisterHeader()).to_be_visible()
        expect(self.getRegisterHeader()).to_have_text("Register")
        self.getFirstNameTextbox().fill(fName)
        self.getLastNameTextbox().fill(LName)
        self.getEmailTextbox().fill(email)
        self.getPhoneNumber().fill(Phone_no)
        self.getOccupationDropdown().select_option(Occupation)
        if gender == "Male":
            self.getGenderMale().click()
        elif gender == "Female":
            self.getGenderFemale().click()
        self.getPassword().type(password)
        self.getConfirmPassword().type(confirmpassword)
        self.getIAm18YearsOrOlderCheckbox().check()
        self.getRegisterButton().click()