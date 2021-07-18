import time
from faker import Faker
from selenium import webdriver
from utilities.BaseClass import BaseClass
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from time import sleep

class Test_Basic(BaseClass):

    def test_sample(self):
        log = self.getLogger()
        faker = Faker()
        name = faker.first_name()
        self.driver.find_element_by_css_selector("[name='name']").send_keys(name)
        log.info("Entered FirstName as "+name)
        assert 'ProtoCommerce' in self.driver.title
        """
        button_text=driver.find_element_by_class_name('btn-default')
        print (button_text.get_attribute ('innerHTML'))
        assert 'Show Message' in driver.page_source
        """
        time.sleep(5)
        self.driver.refresh()

