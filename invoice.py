from public_data import *

# for solving captcha
import pytesseract
from PIL import Image


class Invoice:
    def __init__(self, toolkit, driver, account_number):
        # passing toolkit & driver >> notice not init new ones
        self.toolkit = toolkit
        self.driver = driver
        self.account_number = account_number
        self.total_amount: str
        self.invoice_date: str
        self.payment: str

        # page 1
        self.go_myservices_page()
        # TODO: be sure page in english (selector changes if language is arabic)
        self.input_account_num()
        self.click_view_bill()
        self.solve_captcha()
        self.click_view_bill()
        self.click_detailed_view()
        self._get_meat()

    def go_myservices_page(self):
        # navigate to myservices page
        self.driver.get('https://myservices.se.com.sa/sap/bc/ui5_ui5/sap/zumcui5_mobile/index.html#/Logon')

    def input_account_num(self):
        # wait for the input field for `Enter your Contract Account` to show up
        self.toolkit.wait(xpath['account_num'])

        # enter Contract Account number
        self.toolkit.input_field(xpath['account_num'], self.account_number)

    def click_view_bill(self):
        # click `view bill`
        self.toolkit.click(xpath['view_bill'])

    def solve_captcha(self):
        # wait for captcha to show up
        self.toolkit.wait(xpath['captcha_img'])

        # get captcha numbers
        self.toolkit.capture(xpath['captcha_img'], 'captcha.png')

        # solve captcha
        captcha_num = pytesseract.image_to_string(Image.open('captcha.png'))

        # enter captcha
        self.toolkit.input_field(xpath['captcha_input'], captcha_num)

    def click_detailed_view(self):
        # Solved problem: sometime current invoice is the prevoice one because it takes time to pull new data
        # wait for current invoice account number to match the account number we are working on
        self.toolkit.wait_text(xpath['detailed_view_account_num'], self.account_number)

        # click `detailed view`
        self.toolkit.click(xpath['detailed_view'])

    def _get_meat(self):
        # wait for `total amount` to show up
        self.toolkit.wait(xpath['total_amount'])

        self.total_amount = self.driver.find_element_by_xpath(xpath['total_amount']).text
        # '2,254.22' to '2254.22'
        self.total_amount = self.total_amount.replace(',', '')

        # PROBLEM: invoice_date xpath changes sometimes between id=__text42 and id=__text43.
        # I used jQuary to get
        #   1. the parent sibling element by its text (there are 19 places in dom tree that contains Invoice Date')
        #      so I used last()
        #   2. the parent element and its text
        self.invoice_date = self.driver.execute_script("""return $( "div:contains('Invoice Date')" ).last().next().text()""")

        if self.toolkit.is_exist(xpath['is_paid']):
            self.payment = 'سدد'
        else:
            self.payment = 'غير مسدد'
