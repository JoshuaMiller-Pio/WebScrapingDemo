from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time

with open("TestFile.csv", mode="w", newline='') as csvfile:
    fieldnames = ["item", "price"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    driver = webdriver.Chrome()

    driver.get("https://www.blankedforsafty.co.za/")
    search = driver.find_element(By.ID, "search")

    #sends the key test
    search.send_keys("notebooks")
    #send the enter key which searches
    search.send_keys(Keys.ENTER)

    #looking for page numbers
    pageNums = driver.find_element(By.CLASS_NAME,"page")
    pageNums = pageNums.find_elements(By.TAG_NAME, "list")

    for pageNum in pageNums:
        #looks for an element for the ID of shopfront-app and prints that
        page = driver.find_element(By.CLASS_NAME,"Categorypr0ducts")

        items = page.find_elements(By.CLASS_NAME, "items")

        for item in items:
            name = item.find_element(By.CLASS_NAME, "productNames")
            try:
                price = item.find_element(By.CLASS_NAME, "price")
                print(price.text)
                writer.writerow({"item": name.text, "price": price.text})
            except:
                writer.writerow({"item": name.text, "price": "not in stock/Unavilable"})
                print("not in stock/Unavilable")

        nextButton = page.find_element(By.CLASS_NAME,"nextButton")
        nextButton.click()


time.sleep(5)
driver.quit()