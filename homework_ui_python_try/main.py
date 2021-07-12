# from selenium.webdriver.chrome import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

base_url = "https://www.one.co.il/"
# driver = webdriver.chrome.webdriver.WebDriver(
#     executable_path='C:\\automation\\drivers\\chromedriver.exe')
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get(base_url)