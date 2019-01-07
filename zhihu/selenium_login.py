# -*- coding: utf-8 -*-
from selenium import webdriver
from pickle import dump, load
import pickle
from os.path import exists
from scrapy.selector import Selector
import time
import settings





def login(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver_path = settings.DRIVER_PATH
    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
    browser.get(url)
    t_selector = Selector(text=browser.page_source)
    browser.find_element_by_css_selector(".SignContainer-switch span").click()
    browser.find_element_by_css_selector(".Login-qrcode button").click()

    print("请在30s内扫二维码，我们将为您保存cookies")
    time.sleep(30)
    cookies = browser.get_cookies()
    browser.close()
    pickle.dump(cookies, open(settings.COOKIES_FILENAME, "wb"))



def get():
    cookies = load(open(settings.COOKIES_FILENAME, "rb"))
    return {cookie['name']: cookie['value'] for cookie in cookies}

if __name__ == '__main__':
    login("https://www.zhihu.com")

