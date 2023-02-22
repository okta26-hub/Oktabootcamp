import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_login(self):
        # steps
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin") # isi email
        time.sleep(1)
        self.driver.find_element(By.NAME, "password").send_keys("admin123") # isi password
        time.sleep(1)    
        self.driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click() # button login
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='PIM']").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "firstName").send_keys("asus") # isi nama first name
        time.sleep(1)
        self.driver.find_element(By.NAME, "middleName").send_keys("tuf") # isi nama first name
        time.sleep(1)
        self.driver.find_element(By.NAME, "lastName").send_keys("a15") # isi nama first name
        time.sleep(1)

        # Klik tombol untuk upload foto
        upload_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.oxd-icon-button.employee-image-action')))
        upload_button.click()
        time.sleep(3)

        # Upload file
        file_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        self.driver.execute_script("arguments[0].setAttribute('value', arguments[1])", file_input, 'C:/Users/asus/Desktop/sample.jpg')


        # Close dialog open file dan klik area di luar dialog
        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-oxd-id="btnEmployeeSave"]')
        submit_button.click()


        self.driver.find_element(By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--ghost[data-v-7e88b27e][data-v-4e1a259a]").click() #klik cancel
        time.sleep(8)
       

    def tearDown(self):
        self.driver.quit()
        

if __name__ == "__main__":
    unittest.main()
