class LoginTestData:

    URL = "https://rahulshettyacademy.com/client"

    validCredentials = [{"email": "ramananram449@gmail.com", "password": "Learning@123"},
                        {"email": "testacc01@gmail.com", "password": "Learning@123"},
                        {"email": "testacc02@gmail.com", "password": "Learning@123"}]

    invalidPassword = [{"email":"testacc01@gmail.com", "password": "helloworld"}]

    passwordReset = [{"email":"testacc01@gmail.com", "password":"Learning@123", "confirmpassword": "Learning@123"}]

    registerData = [{"FirstName": "Test",
                     "LastName": "Acc02",
                     "Email": "testacc02@email.com",
                     "Phone_No": "8144551058",
                     "Occupation": "3: Engineer",
                     "Gender": "Male",
                     "Password": "Learning@123",
                     "ConfirmPassword": "Learning@123"}]