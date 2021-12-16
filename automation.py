from selenium import webdriver
import time

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')

# assert 'Selenium Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title
# show_message_button = chrome_browser.find_element_by_class_name("btn btn-default")

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Hello there darling')

time.sleep(1)
close_popup = chrome_browser.find_element_by_id('at-cv-lightbox-close')
close_popup.click()

time.sleep(1)
show_message_button = chrome_browser.find_element_by_css_selector('btn')
show_message_button.click()


time.sleep(5)
chrome_browser.close()