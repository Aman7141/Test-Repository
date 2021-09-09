from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C://webdrivers/chromedriver.exe")

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")

# how to switch to frames or iframes
# switching to frame using frame name

driver.switch_to.frame("classFrame")  # 3rd frame
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)

driver.switch_to.frame("packageFrame")  # 2nd frame
driver.find_element_by_link_text("AcceptAlert").click()

driver.switch_to.default_content()
time.sleep(3)

driver.switch_to.frame("packageListFrame")  # 1st frame
driver.find_element_by_link_text("org.openqa.selenium.edge").click()
