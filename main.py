from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('window-size=1000,1080')

driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(3)

driver.get(url='https://w3.assembly.go.kr/')
driver.implicitly_wait(2)

driver.find_element_by_css_selector('#bodycont > div > div.listbox > ul > li:nth-child(1) > a')

sample = driver.find_element_by_class_name('contentBox_02 ')
sample.send_keys('\n')

#element = driver.find_element_by_xpath('//*[@id="bodycont"]/div/div[2]/ul/li[1]/a')
#print(element.is_enabled())

#driver.find_element_by_xpath('//*[@id="bodycont"]/div/div[2]/ul/li[1]/a').click()



sleep(3)
driver.close()