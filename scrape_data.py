# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:01:25 2023

@author: SA
"""

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas as pd
import os

# Create a global variable
year_text = []
model_text = []
length_text = []
width_text = []
height_text = []
color_text = []
id_text = []


try:
    
    # =============================================================================
    # Disable chrome items
    # =============================================================================
    # end_pro.set("")
    # profile = "C:\\Users\\Faizan\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 25"
    # uc.TARGET_VERSION = 116 
    options = uc.ChromeOptions()
    options.add_argument('--disable-notifications')
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")
    # New Here
    options.add_argument('--disable-gpu')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("user-data-dir={}".format(profile))
    # options.add_argument("--incognito")
    # =============================================================================
    # End items
    # =============================================================================
    driver = uc.Chrome(options=options, use_subprocess=True,version_main = 116)
    
    browser_status = True
    
except Exception as e:
    browser_status = False
    print("Browser Open Fail! : ", e)
    

if browser_status == True:
    driver.get(f'https://car-dimensions-tool.com/en/make/')
    

    # ---------------------------------
    # Form File Data Scrape
    elements = driver.find_elements(By.TAG_NAME, value="a")

    # elem = driver.find_elements(By.CLASS_NAME, value="custom-page")
    # ad = len(elem)
    # cnn = 0
    # for i in elem:
    #     # form_file_txt.append(i.text)
    #     cnn = cnn + 1
    #     if cnn == 0:
    #         print("skip")
    #     else:
    #         print(i.text)
    #         id_text.append(i.text)
        
    # print(id_text)
        
    links = []

    for element in elements:
        link = element.get_attribute('href')
        if link:
            links.append(link)
    
    
    site_link = []
    # print(links)
    for i in links:
        # form_file_txt.append(i.text)
        if ((i == "https://car-dimensions-tool.com/en/make/acura"
        or i == "https://car-dimensions-tool.com/en/make/alfa-romeo"
        or i == "https://car-dimensions-tool.com/en/make/alpine"
        or i == "https://car-dimensions-tool.com/en/make/artega"
        or i == "https://car-dimensions-tool.com/en/make/aston-martin"
        or i == "https://car-dimensions-tool.com/en/make/audi"
        or i == "https://car-dimensions-tool.com/en/make/bentley"
        or i == "https://car-dimensions-tool.com/en/make/bmw"
        or i == "https://car-dimensions-tool.com/en/make/bugatti"
        or i == "https://car-dimensions-tool.com/en/make/buick"
        or i == "https://car-dimensions-tool.com/en/make/cadillac"
        or i == "https://car-dimensions-tool.com/en/make/chevrolet"
        or i == "https://car-dimensions-tool.com/en/make/chrysler"
        or i == "https://car-dimensions-tool.com/en/make/citroen"
        or i == "https://car-dimensions-tool.com/en/make/dacia"
        or i == "https://car-dimensions-tool.com/en/make/dodge"
        or i == "https://car-dimensions-tool.com/en/make/ferrari"
        or i == "https://car-dimensions-tool.com/en/make/fiat"
        or i == "https://car-dimensions-tool.com/en/make/ford"
        or i == "https://car-dimensions-tool.com/en/make/genesis"
        or i == "https://car-dimensions-tool.com/en/make/gmc"
        or i == "https://car-dimensions-tool.com/en/make/honda"
        or i == "https://car-dimensions-tool.com/en/make/hyundai"
        or i == "https://car-dimensions-tool.com/en/make/infiniti"
        or i == "https://car-dimensions-tool.com/en/make/isuzu"
        or i == "https://car-dimensions-tool.com/en/make/jaguar"
        or i == "https://car-dimensions-tool.com/en/make/jeep"
        or i == "https://car-dimensions-tool.com/en/make/kia"
        or i == "https://car-dimensions-tool.com/en/make/lada"
        or i == "https://car-dimensions-tool.com/en/make/lamborghini"
        or i == "https://car-dimensions-tool.com/en/make/land-rover"
        or i == "https://car-dimensions-tool.com/en/make/lexus"
        or i == "https://car-dimensions-tool.com/en/make/lincoln"
        or i == "https://car-dimensions-tool.com/en/make/lotus"
        or i == "https://car-dimensions-tool.com/en/make/maserati"
        or i == "https://car-dimensions-tool.com/en/make/mazda"
        or i == "https://car-dimensions-tool.com/en/make/mclaren"
        or i == "https://car-dimensions-tool.com/en/make/mercedes"
        or i == "https://car-dimensions-tool.com/en/make/mini"
        or i == "https://car-dimensions-tool.com/en/make/mitsubishi"
        or i == "https://car-dimensions-tool.com/en/make/nissan"
        or i == "https://car-dimensions-tool.com/en/make/opel"
        or i == "https://car-dimensions-tool.com/en/make/peugeot"
        or i == "https://car-dimensions-tool.com/en/make/polestar"
        or i == "https://car-dimensions-tool.com/en/make/porsche"
        or i == "https://car-dimensions-tool.com/en/make/ram"
        or i == "https://car-dimensions-tool.com/en/make/renault"
        or i == "https://car-dimensions-tool.com/en/make/rolls-royce"
        or i == "https://car-dimensions-tool.com/en/make/seat"
        or i == "https://car-dimensions-tool.com/en/make/skoda"
        or i == "https://car-dimensions-tool.com/en/make/smart"
        or i == "https://car-dimensions-tool.com/en/make/ssangyong"
        or i == "https://car-dimensions-tool.com/en/make/subaru"
        or i == "https://car-dimensions-tool.com/en/make/suzuki"
        or i == "https://car-dimensions-tool.com/en/make/tesla"
        or i == "https://car-dimensions-tool.com/en/make/toyota"
        or i == "https://car-dimensions-tool.com/en/make/vauxhall"
        or i == "https://car-dimensions-tool.com/en/make/volkswagen"
        or i == "https://car-dimensions-tool.com/en/make/volvo"
    )):
            print(i)
            site_link.append(i)
    
    cnn = 0
    cnn_text = []
    print(site_link)
    
    for site in site_link:
        print(site)
        driver.get(site)
    # driver.get(site_link[0])
        sleep(3)
        cnn = cnn + 1
        

        # ----------------------------------
        # Model Data Scrape
        # model = driver.find_elements(By.CLASS_NAME, value="mdl_link")
        
        # for i in model:
        #     print(i.text)
        
        # # ----------------------------------
        # # Length model Data Scrape
        # length = driver.find_elements(By.CLASS_NAME, value="mat_css fmic")
        
        # for i in model:
        #     print(i.text)

        # # ----------------------------------
        # # Model Data Scrape
        # model = driver.find_elements(By.CLASS_NAME, value="mdl_link")
        
        # for i in model:
        #     print(i.text)

        # # ----------------------------------
        # # Model Data Scrape
        # model = driver.find_elements(By.CLASS_NAME, value="mdl_link")
        
        # for i in model:
        #     print(i.text)
            
        # Pagination applied from here
        reporting = driver.find_elements(By.CLASS_NAME, value="paginate_button")
        # print(reporting.text)
        # reporting[2].click()
        report = len(reporting)
        count = 0
        sleep(5)
        # # abc = driver.find_element(By.CLASS_NAME, value = "//*[@id=\"cardata_paginate\"]/span/a[3]")
        for i in reporting:
            sleep(2)
            reporting = driver.find_elements(By.CLASS_NAME, value="paginate_button")

            # Locate the table element
            table = driver.find_element(By.XPATH, "//*[@id=\"cardata\"]")

            
            # Find all rows within the table
            rows = table.find_elements(By.TAG_NAME, value="tr")
            
            # Initialize an empty list to store the data
            data = []
            
            # Loop through each row and extract data from each cell
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, value="td")  # Use "th" if it's a header row
                row_data = [cell.text for cell in cells]
                data.append(row_data)
            
            table_data = len(data)
            
            cnt = 0
            # print(data)
            print(data[0])

            for i in range(0,table_data - 1):
                cnt = int(cnt) + 1
                print(cnt)
                result = data[int(cnt)]
                model_text.append(result[0])
                year_text.append(result[1])
                length_text.append(result[2])
                width_text.append(result[3])
                height_text.append(result[4])
                color_text.append(result[7])
                cnn_text.append(cnn)


            if count == report - 1 or count == 0 or count == 1:
                print("skip")
            else:
                # driver.find_element(By.XPATH, value = f"//*[@id=\"cardata_paginate\"]/span/a[{count}]").click()
                # print(i.text)
                # print(reporting[count])
                # i.click()
                reporting[count].click()
                sleep(3)
            count = count + 1

print(len(cnn_text))
print(len(model_text))
print(len(year_text))
print(len(length_text))
print(len(width_text))
print(len(height_text))
print(len(color_text))

dictionary = {
"Id" : cnn_text,
"Model" : model_text,
"Year" : year_text,
"Length" : length_text,
"Width" : width_text,
"Height" : height_text,
"Color" : color_text
}
df = pd.DataFrame(dictionary)

excel_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "excel_path")
df.to_excel(r'/Users/abdulhaseeb/Downloads/File_Name.xlsx', index = False)
print("File generated")   
    