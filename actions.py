from selenium import webdriver
import time


def open_driver():
    return webdriver.Firefox(executable_path=r'C:\Users\singh\Downloads\geckodriver')


def cutshort_scrapper():

    driver = open_driver()
    driver.get('https://cutshort.io/')

    login_button = driver.find_element_by_css_selector('div.everyOtherSubtleButton > div:nth-child(1)')
    login_button.click()

    time.sleep(2)

    google_login_button = driver.find_element_by_css_selector('.google_login_bg > div:nth-child(1) > div:nth-child(2) '
                                                              '> div:nth-child(1)')
    google_login_button.click()

    google_login_id = driver.find_element_by_css_selector('#identifierId')
    google_login_id.click()
    time.sleep(1)
    google_login_id.send_keys('yashyashbor@gmail.com')
    google_next_button = driver.find_element_by_css_selector('.VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)')
    google_next_button.click()
    time.sleep(2)
    
    time.sleep(5)
