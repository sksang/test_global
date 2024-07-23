import pytest
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
import time


def test_a():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    cdm = ChromeDriverManager().install()
    driver = webdriver.Chrome("chromedriver", options=options)

    driver.get("https://discuss.python.org/t/understanding-site-packages-directories/12959")
    time.sleep(5)
    print(driver.title)
