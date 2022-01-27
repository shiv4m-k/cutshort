from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def open_driver():
    return webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe')

def cutshort_scrapper():
    driver = open_driver()
    driver.get('https://cutshort.io/')

    login_button = driver.find_element_by_css_selector('div.everyOtherSubtleButton > div:nth-child(1)')
    login_button.click()
    time.sleep(2)
    google_login_button = driver.find_element_by_css_selector('.google_login_bg > div:nth-child(1) > div:nth-child(2) '
                                                              '> div:nth-child(1)')
    google_login_button.click()

    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])

    google_login = driver.find_element_by_xpath('//*[@id="identifierId"]')
    google_login.send_keys('roshini@getdefault.in')
    google_login_next = driver.find_element_by_class_name('VfPpkd-RLmnJb')
    google_login_next.click()
    time.sleep(2)

    google_pass = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    google_pass.click()
    time.sleep(1)
    google_pass.send_keys('Roshini@default')

    google_pass_next = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')

    google_pass_next.click()
    time.sleep(10)

    view_jobs = driver.find_element_by_xpath('//*[@id="main_nav_item_matchingjobs"]/a')
    #view_jobs.click()
    time.sleep(2)


    time.sleep(5)
