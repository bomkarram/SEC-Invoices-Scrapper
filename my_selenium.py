# my toolkit for selenium
# this toolkit has the main driver + shortcut functions for repetitive code

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

# for explicit waiting
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# if element not exist
from selenium.common.exceptions import NoSuchElementException

class Toolkit:
    def __init__(self):
        self._set_options()

        # init browser
        self.driver = Chrome(executable_path='./chromedriver', options=self.options)

    def _set_options(self):
        self.options = Options()

        # go headless
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        self.options.add_argument('--headless')
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument('--ignore-ssl-errors')
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--window-size=1280,1000')
        self.options.add_argument('--allow-insecure-localhost')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument('--no-sandbox')

        # don't load images
        self.options.add_argument('--blink-settings=imagesEnabled=false')

        # scrape using disk cache: faster
        prefs = {'disk-cache-size': 4096}
        self.options.add_experimental_option('prefs', prefs)

    def wait(self, xpath):
        try:
            return WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
        except Exception as e:
            print(e)

    def wait_text(self, xpath, text):
        try:
            return WebDriverWait(self.driver, 30).until(
                EC.text_to_be_present_in_element((By.XPATH, xpath), text)
            )
        except Exception as e:
            print(e)

    def click(self, xpath):
        clickable = self.driver.find_element_by_xpath(xpath)
        clickable.click()

    def input_field(self, xpath, value):
        input_field = self.driver.find_element_by_xpath(xpath)
        input_field.send_keys(value)

    def capture(self, xpath, image_path):
        captcha = self.driver.find_element_by_xpath(xpath)
        captcha.screenshot(image_path)

    def is_exist(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
            return True
        except NoSuchElementException:
            return False
