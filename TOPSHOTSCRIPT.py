from selenium import webdriver
import time
from fake_useragent import UserAgent

email = input("Please input email: ")
ua = UserAgent()
userAgent = ua.random
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'user-agent={"userAgent"}')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=chrome_options,executable_path=r"C:\\Users\\amera\\Downloads\\chromedriver.exe")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
driver.get("https://www.stackoverflow.com/")
time.sleep(3)
driver.find_element_by_xpath("/html/body/header/div/ol[2]/li[2]/a[2]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='openid-buttons']/button[1]").click()
time.sleep(1)
driver.find_element_by_id("identifierId").send_keys(email)
time.sleep(1)
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
time.sleep(1)
driver.get("https://www.nbatopshot.com/")
time.sleep(3)
driver.find_element_by_link_text("SIGN UP").click()
time.sleep(3)
driver.find_element_by_class_name("css-1u05wcl").click()
time.sleep(1)
driver.find_element_by_id("identifierId").send_keys(email)
time.sleep(1)
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()





