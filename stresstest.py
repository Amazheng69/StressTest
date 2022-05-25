from selenium import webdriver
import selenium.webdriver.chrome.service as Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

opts = Options()
opts.add_experimental_option("detach", True)
opts.add_argument("--window-size=1920,1080")
opts.add_argument("start-maximized")
opts.add_argument('--headless')
opts.add_argument('--disable-gpu')
opts.add_argument("disable-web-security")
opts.add_argument("allow-running-insecure-content")
capabilities = webdriver.DesiredCapabilities.CHROME.copy();
capabilities = opts.to_capabilities()
#driver=webdriver.Chrome('D:\Monash\Labs\ENG4701 FYP Project A\Code\P2P Energy Blockchain\imdc_p2p_energy_trading\zcustomtest\chromedriver.exe', options=opts, desired_capabilities=capabilities)
driver=webdriver.Chrome("/usr/bin/chromedriver",  options=opts, desired_capabilities=capabilities)
driver.get('http://p2penergytrading.loca.lt/login')
time.sleep(3)
# driver.save_screenshot('ss.png')
# screenshot=Image.open('ss.png')
# screenshot.show()

WebElement_username=driver.find_element(By.ID,"username")
time.sleep(3)
WebElement_password=driver.find_element(By.ID,"password")
WebElement_username.send_keys("WZH")
WebElement_password.send_keys("473633")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//a[@href='/order']").click()
time.sleep(9)
WebElement_energyAmount=driver.find_element_by_id("energyAmount").send_keys(Keys.BACK_SPACE,"5")
time.sleep(1)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='Confirm']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='OK']").click()
