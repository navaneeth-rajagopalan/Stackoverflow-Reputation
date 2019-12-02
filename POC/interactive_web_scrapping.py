from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
#options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

#launch url
url = "https://data.stackexchange.com/stackoverflow/query/1160769?Location=Sydney"

driver.implicitly_wait(30)
driver.get(url)

try:
    run_btn = driver.find_element_by_id('submit-query')
    run_btn.click()
except:
    print("An exception occurred")


csv_file_url_id = "resultSetsButton"

try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "query-results"))
    )
finally:
    csv_url = driver.find_element_by_id('resultSetsButton').get_attribute("href")
    print(csv_url)
    data = pd.read_csv(csv_url)
    data.to_csv("Test.csv", sep='\t', encoding='utf-8')