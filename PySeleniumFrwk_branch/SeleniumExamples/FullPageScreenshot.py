from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
# chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options)
# driver.get("http://www.way2automation.com/")
# driver.get("https://www.udemy.com/")
driver.maximize_window()
driver.implicitly_wait(1)
scroll = lambda exp: driver.execute_script('return document.body.parentNode.scroll' + exp)
driver.set_window_size(scroll('Width'), scroll('Height'))
driver.find_element_by_tag_name('body').screenshot('./screenshot/fullpage3.jpg')


