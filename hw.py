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
        name = svet.find_element(By.CSS_SELECTOR, "a.ui-GPFV8").text
        price = svet.find_element(By.CSS_SELECTOR, "span.ui-LD-ZU.KIkOH").text
        link = svet.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
    except:
        print("Parsing error")
        continue

    parsed_data.append([name, price, link])

driver.quit()

for i in range(len(parsed_data)):
    parsed_data[i][1] = float(parsed_data[i][1].replace("руб.", "").strip().replace(" ", ""))

with open("svet.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "price", "link"])
    writer.writerows(parsed_data)
