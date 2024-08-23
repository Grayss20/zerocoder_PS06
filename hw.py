import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.divan.ru/category/svet"

driver.get(url)

time.sleep(5)

svets = driver.find_elements(By.CSS_SELECTOR, "div.wYUX2")

parsed_data = []

for svet in svets:
    try:
        name = svet.find_element(By.CSS_SELECTOR, "a span::text")
        price = svet.find_element(By.CSS_SELECTOR, "span.ui-LD-ZU.KIkOH::text")
        link = svet.find_element(By.CSS_SELECTOR, "a::attr(href)")
    except:
        print("Parsing error")
        continue

    parsed_data.append([name, price, link])

driver.quit()

with open("svet.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "price", "link"])
    writer.writerows(parsed_data)
