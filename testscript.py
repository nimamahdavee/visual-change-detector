from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")


service = Service()


driver = webdriver.Chrome(service=service, options=options)

try:
    
    driver.get("https://www.google.com")
    time.sleep(2)  # صبر برای بارگذاری کامل

    driver.save_screenshot("google_shot1.png")
    print("Screenshot 1 saved.")

    time.sleep(3)


    driver.save_screenshot("google_shot2.png")
    print("Screenshot 2 saved.")

finally:
    driver.quit()
