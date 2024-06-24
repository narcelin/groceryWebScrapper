from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import requests

from bs4 import BeautifulSoup

import time

def main():

    print("Scrapper Starting")

    pubURL = "https://www.publix.com/mc/order-ahead/landing?bannerid=1_oa_oa-bc_bc_oa-lp_x&nav=header&page=1"

    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome()
    driver.get(pubURL)

    # store_locator_search_input_element = driver.find_element(By.CSS_SELECTOR(""))

    # WebDriverWait(driver, 10)

    # content = driver.page_source.encode('utf-8').strip()
    # print(content)

    time.sleep(50)

    # print("Hello, Scrapper!")


    # soup = BeautifulSoup(content, "html.parser")
    # elements = soup.find_all(class_="")

    # print(soup)

if __name__ == "__main__":
    main()