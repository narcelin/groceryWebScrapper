from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException

import re

import requests

from bs4 import BeautifulSoup

import time

def main():

    print("Scrapper Starting")

    alURL = "https://shop.aldi.us/store/aldi/storefront"

    op = webdriver.ChromeOptions()
    op.add_argument('headless')

    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(options=op)

    driver.get(alURL)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "e-10zhp0q"))
        )

    # Selects deliver and pickup elements. [0] for delivery, [1] for pickup
    pickup_button_element = driver.find_elements(By.CLASS_NAME, "e-10zhp0q")[1]
    pickup_button_element.click()

    VIEW_ALL_CLASS_NAME = "e-181dj89"
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, VIEW_ALL_CLASS_NAME))
        )

    view_all_elements = driver.find_elements(By.CLASS_NAME, VIEW_ALL_CLASS_NAME)

    

    # time.sleep(10)
    view_all_elements[0].click()

    ################################################################################################################

    # Need to add scroll so that all information is loaded before retrieving


    PRODUCTS_OVERLAY_CONTAINER_CLASS_NAME = "e-b9ufyr"
    LOAD_MORE_BUTTON_ELEMENT_CLASS_NAME = "e-1ezcq1y"

    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, PRODUCTS_OVERLAY_CONTAINER_CLASS_NAME))
    )

    product_overlay_container_element = driver.find_element(By.CLASS_NAME, PRODUCTS_OVERLAY_CONTAINER_CLASS_NAME)

    time.sleep(3)

    button_exists = 1
    while(button_exists):
        try:
            print("Try catch ran")
            load_more_button_element = driver.find_element(By.CLASS_NAME, LOAD_MORE_BUTTON_ELEMENT_CLASS_NAME)
            load_more_button_element.click();
        except NoSuchElementException:
            print("No more loading buttons")
            button_exists = 0

    WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "screen-reader-only"))
    )
 
    product_container_elements = product_overlay_container_element.find_elements(By.TAG_NAME, "li")
    print(product_container_elements[0].text)

    exit()

    product_screen_reader_price_elements = product_overlay_container_element.find_elements(By.CLASS_NAME, "screen-reader-only")

    print(product_screen_reader_price_elements[0].text)

    pattern = r"\$\d+.\d+"
    match = re.search(pattern, product_screen_reader_price_elements[0].text)

    # group returns the string. [1:] slices the first character. [start:end]
    print(match.group()[1:])
    
    for product in product_screen_reader_price_elements:
        print("Starting loop")
        print(product.text)

        pattern = r"\$\d+.\d+"
        match = re.search(pattern, product.text)

        # group returns the string. [1:] slices the first character. [start:end]
        print(match.group()[1:])

    ################################################################################################################


    time.sleep(50)

if __name__ == "__main__":
    main()