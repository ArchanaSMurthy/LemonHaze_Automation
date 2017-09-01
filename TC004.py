from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.firefox import webelement

driver_path = "D:\chromedriver_win32" + "\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--test-type')

driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
driver.get("https://lemonhaze.com/")


time.sleep(2)


driver.find_element_by_link_text("Sign in").click()
username=driver.find_element_by_id("user_email")
password=driver.find_element_by_id("user_password")
btnSignup=driver.find_element_by_css_selector("input[type='submit'][value='Sign in']")

username.send_keys("manu@celestialsys.com")
password.send_keys("Rishi@501")
btnSignup.click()
time.sleep(2)
driver.find_element_by_link_text("Products").click()
time.sleep(2)
driver.find_element_by_xpath("//a[text()='Sativa Flower']").click()
time.sleep(3)
follow_loop = range(1, 251)
for x in follow_loop:
    elements=driver.find_element_by_xpath("//div[text()='Top 250 Indica Flower']//following::div[@class='row lmn-top-list-row align-items-center']["+str(x)+"]//div[@class='bg-logo']")
    image = elements.find_element_by_tag_name('img')
    img_src = image.get_attribute("src")
    abc=img_src.split("/")
    imagnologo='placeholder.png'
    if abc[5]!=imagnologo:
      print(str(x)+" "+abc[5]+" "+"Pass")
    else:
      print(str(x)+" "+abc[5]+" "+"Fail"+" "+"Logo is not present")  
driver.close() 
       