from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
from Test_Data import data
from Test_Locators import locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException



class Test_project2:
    @pytest.fixture
    def startup(self):
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.quit()

#FORGOT PASSWORD LINK VALIDATION
    def test_forgot_password(self,startup):
        self.wait=WebDriverWait(self.driver,20)
        self.driver.get(data.Data().url)
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.Locators().forgot))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Locators().username_input_box))).send_keys(data.Data().username1)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.Locators().reset))).click()
            self.url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset"
            if self.driver.current_url==self.url:
                print("Reset link sent Successfully")
            else:
                print("Failed")
        except NoSuchElementException:
            print("element missing")


#METHOD1: FOR VALIDATING HEADER IN ADMIN PAGE           
    def test_method1_title_admindisplay(self, startup):
        self.driver.get(data.Data().url)
        self.wait=WebDriverWait(self.driver,20)
        try:
            self.driver.implicitly_wait(10)
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Locators().username_input_box))).send_keys(data.Data().username)
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Locators().password_input_box))).send_keys(data.Data().valid_password )
            self.driver.find_element(By.XPATH,locators.Locators().submit_button).click()

#title validation           
            actual_title=self.driver.title
            expected_title="OrangeHRM"
            if actual_title == expected_title:
                print("TITLE VALIDATION IS SUCCESS")

#header validation on admin page            
            A=self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.Locators().admin)))
            A.click()
            list1=self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.Locators().header)))
            print((list1).text)
            print("All ELEMENTS IN HEADER ADMIN PAGE ARE DISPLAYED SUCCESSFULLY")
        except TimeoutException:
            print("element missing")


#METHOD2: FOR VALIDATING HEADER IN ADMIN PAGE
    def test_method2_displayadmin(self,startup):
        self.driver.get(data.Data().url)
        self.wait=WebDriverWait(self.driver,20)
        try:
            self.driver.implicitly_wait(10)
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Locators().username_input_box))).send_keys(data.Data().username)
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Locators().password_input_box))).send_keys(data.Data().valid_password )
            self.driver.find_element(By.XPATH,locators.Locators().submit_button).click()
            A=self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.Locators().admin)))
            A.click()
            l1=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Locators().user))).text
            print(f"{l1} is Displayed")
            l2=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Locators().job))).text
            print(f"{l2} is Displayed")
            l3=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Locators().org))).text
            print(f"{l3} is Displayed")
            l4=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Locators().quali))).text
            print(f"{l4} is Displayed")
            l5=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Locators().nation))).text
            print(f"{l5} is Displayed")
            l6=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Locators().corporate))).text
            print(f"{l6} is Displayed")
            l7=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Locators().config))).text
            print(f"{l7} is Displayed")
            print("ALL ELEMENTS IN HEADER ADMIN PAGE ARE DISPLAYED SUCCESSFULLY")
        except NoSuchElementException:
            print("element missing")



#VALIDATING MAIN MENU ON ADMIN PAGE
    def test_main_menu_validation(self,startup):
        self.driver.get(data.Data().url)
        self.wait=WebDriverWait(self.driver,30)
        try:
            self.driver.implicitly_wait(10)
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Locators().username_input_box))).send_keys(data.Data().username)
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Locators().password_input_box))).send_keys(data.Data().valid_password )
            self.driver.find_element(By.XPATH,locators.Locators().submit_button).click()
            l1=self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.Locators().admin1))).text
            print(f"{l1} is Displayed")
            l2=self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.Locators().pim))).text
            print(f"{l2} is Displayed")
            l3=self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.Locators().leave))).text
            print(f"{l3} is Displayed")
            l4=self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.Locators().time))).text
            print(f"{l4} is Displayed")
            l5=self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.Locators().recruitment))).text
            print(f"{l5} is Displayed")
            l6=self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.Locators().myinfo))).text
            print(f"{l6} is Displayed")
            l7=self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.Locators().perform))).text
            print(f"{l7} is Displayed")
            l8=self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.Locators().dashboard))).text
            print(f"{l8} is Displayed")
            l9=self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.Locators().directory))).text
            print(f"{l9} is Displayed")
            l10=self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.Locators().maintenance))).text
            print(f"{l10} is Displayed")
            l11=self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.Locators().claim))).text
            print(f"{l11} is Displayed")
            l12=self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.Locators().buzz))).text
            print(f"{l12} is Displayed")
            print ("MAIN MENU VALIDATION IS SUCCESS")
        except TimeoutException:
            print("element missing")