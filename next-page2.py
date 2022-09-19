from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Utility\BrowserDrivers\chromedriver.exe')
driver.get('https://hidemyna.me/en/proxy-list/')
while True:
    try:
        driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='arrow__right']/a"))))
        driver.find_element_by_xpath("//li[@class='arrow__right']/a").click()
        print("Navigating to Next Page")
    except (TimeoutException, WebDriverException) as e:
        print("Last page reached")
        break
driver.quit()