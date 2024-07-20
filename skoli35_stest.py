import time
from selenium import webdriver

coptions = webdriver.ChromeOptions()

coptions.add_argument("--headless")

driver = webdriver.Chrome(options=coptions)

driver.get("https://olympics.com/en/paris-2024")

driver.maximize_window()

time.sleep(5)

print(f"\nTotle: {driver.title}")
