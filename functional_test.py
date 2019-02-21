from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://localhost:8000')
time.sleep(6)

assert 'Django' in driver.title
driver.quit()
