from pageObjects.UserProfilePage import UserProfile_Class
from utilities import ExcelFileOperation
from utilities.Logger import Logging_class
from utilities.readproperties import Readconfig


class Test_User_Profile_DDT:
    LoginUrl = Readconfig.getLoginUrl()
    RegistrationUrl = Readconfig.getRegistrationUrl()
    Username = Readconfig.getUsername()
    Password = Readconfig.getPassword()
    log = Logging_class.log_generator()
    path = "C:\\Users\\Dreamer\\Documents\\pythonProject1\\pythonProject\\credkartjanproject\\testCases\\TestData\\LoginData.xlsx"

    def test_user_login_ddt(self, setup):
        self.log.info("opening browser")
        self.driver = setup
        self.log.info("Opening URL ")
        self.ur = UserProfile_Class(self.driver)
        self.rows = ExcelFileOperation.rows_count(self.path, 'sheet1')
        print(self.rows)
        List = []
        for r in range(2, self.rows + 1):
            self.email = ExcelFileOperation.ReadData(self.path, 'sheet1', r, 1)
            self.password = ExcelFileOperation.ReadData(self.path, 'sheet1', r, 2)
            self.Exp_Result = ExcelFileOperation.ReadData(self.path, 'sheet1', r, 3)
            self.log.info("------Opening URL Link---------")
            self.driver.get(self.LoginUrl)
            self.log.info("Entering Email ->" + self.email)
            self.ur.Enter_Email(self.email)
            self.log.info("Entering Password ->" + self.password)
            self.ur.Enter_Password(self.password)
            self.ur.Click_Login_Or_RegisterButton()

            if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
                if self.Exp_Result == "Pass":
                    List.append("Pass")
                    self.log.info("Testcase is passed")
                    ExcelFileOperation.WriteData(self.path, 'sheet1', r, 4, "Pass")
                    self.driver.save_screenshot(".\\Screenshots\\Login_Pass.png")
                    self.ur.click_drpdwn_btn()
                    self.ur.click_logout()

                elif self.Exp_Result == "Fail":
                    List.append("Fail")
                    self.log.info("testcase failed")
                    ExcelFileOperation.WriteData(self.path, 'sheet1', r, 4, "Fail")
                    self.driver.save_screenshot(".\\Screenshots\\Login_fail.png")

            else:
                List.append("Fail")
                if self.Exp_Result == "Pass":
                    self.log.info("testcase failed")
                    ExcelFileOperation.WriteData(self.path, 'sheet1', r, 4, "Fail")
                    self.driver.save_screenshot(".Screenshots\\Login_fail.png")

                elif self.Exp_Result == "Fail":
                    List.append("Pass")
                    self.log.info("testcase failed")
                    ExcelFileOperation.WriteData(self.path, 'sheet1', r, 4, "Fail")
                    self.driver.save_screenshot(".\\Screenshots\\Login_fail.png")

                self.driver.save_screenshot(".\\Screenshots\\Login_Fail.png")



        print(List)

# pytest -v --html=pythonProject1/pythonProject/credkartjanproject/HTMLReports/report.html --browser chrome -n=2 --alluredir="C:\Users\Dreamer\Documents\pythonProject1\pythonProject\credkartjanproject\AllureReports"
# allure serve "AllureReports"
