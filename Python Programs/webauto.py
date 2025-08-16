#Script for web automation with SELENIUM
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
print('complete')
driver=webdriver.Chrome(r'/Users/yoezeljai/Downloads/chromedriver')
driver.maximize_window()
driver.get('https://www.facebook.com')
print('complete')
time.sleep(5)
#driver.find_element_by_id('email').send_keys('prakash_12699@yahoo.com')
#driver.find_element_by_id('pass').send_keys('Offl!ne@21')
#driver.find_element_by_css_selector('#u_0_2').click()
driver.find_element_by_xpath('//*[@id="u_0_j"]').send_keys('JAI')
driver.find_element_by_xpath('//*[@id="u_0_l"]').send_keys('PRAKASH')
driver.find_element_by_xpath('//*[@id="u_0_o"]').send_keys('7760672980')
driver.find_element_by_xpath('//*[@id="u_0_v"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="u_0_a"]').click()
sd=Select(driver.find_element_by_id('day'))
sd.select_by_visible_text('21')
sm=Select(driver.find_element_by_id('month'))
sm.select_by_visible_text('Feb')
sy=Select(driver.find_element_by_id('year'))
sy.select_by_visible_text('1991')
var=driver.page_source
driver.close()
