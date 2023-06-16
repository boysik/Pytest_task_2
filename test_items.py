from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_diffirent_languages(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    
