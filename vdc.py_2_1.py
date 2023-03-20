from bs4 import BeautifulSoup
import json
import re
import requests
import time
import datetime
import logging
from dateutil import parser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from unidecode import unidecode
import os
import pandas as pd
import glob
import warnings
import csv
import json
import pymysql
import openpyxl as xl
from openpyxl.styles import Font
from openpyxl.styles import PatternFill

warnings.simplefilter("ignore")
os.chdir("C:/Users/AGL/Downloads")
print(os.getcwd())
from datetime import date
from datetime import timedelta
import pymysql
import xlrd
import pandas as pd
import os
import datetime
import unicodedata

from datetime import date
from datetime import timedelta
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = (
    "C:/Program Files/Google/Chrome Beta/Application/chrome.exe"
)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument(
    "--user-data-dir=C:/Users/AGL/AppData/Local/Google/Chrome Beta/User Data"
)
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(
    "C:/Users/AGL/Downloads/chromedriver_win32 (9)/chromedriver",
    chrome_options=chrome_options,
)
# url_list = 'https://advertising.flipkart.com/ad-account/campaigns?baccount=RSAUFLMCSZ&ascending=false&dropDownVal='
# print('...................',url_list)
# driver.get(url_list)
# time.sleep(120)
url_list = "https://advertising.flipkart.com/ad-account/campaigns/pca/2SSI4JORNFIF?baccount=RSAUFLMCSZ"
print("...................", url_list)
driver.get(url_list)
time.sleep(10)


# # Find the transparent button using an XPath selector
# transparent_button = driver.find_element_by_xpath("//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/header/section/div[2]/div/span[1]/button")

# # Check if the button is displayed on the page
# if transparent_button.is_displayed():
#     # Click the button if it is visible
#     transparent_button.click()

# Close the browser window


# try:
# 	html_container = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/section').get_attribute('innerHTML')
# 	soup = BeautifulSoup(html_container, 'html.parser')
# 	time.sleep(5)
# except Exception as e:
# 	print(e)
# if html_container is not None:
# 			print('went in first interface>>>>>>>>')
# 			soup = BeautifulSoup(html_container, 'html.parser')

# 			# Find the element using class name
# 			element = driver.find_element_by_class_name("styles__TransparentButtonParent-lemv3x-3 jsKpsv")

# 			# Perform a click action on the element
# 			element.click()


# Find the element using XPath
try:
    element = driver.find_element_by_xpath(
        '//div[@class="action"]/*[name()="svg"]'
    ).click()
except Exception as e:
    print(e)

# Check if the element is clickable
if element.get_attribute("onclick"):
    print("Element is clickable")
else:
    print("Element is not clickable")

    # Quit the browser

    # try:
    # 	print('im in try')
    # 	driver.find_element_by_xpath('//*[@id="list"]/div/div/div[2]/div/div[1]/div/div/div/div[9]/div/span[3]/div/svg').click()
    # 	time.sleep(10)
    # 	print('wjshnidiidhni')
    # 	# button.click()
    # except:
    # 	driver.find_element_by_xpath('//*[@id="duration"]/div/span[2]/div/svg').click()

    # try:

    # 	dbconnection1 = pymysql.connect(host='43.204.245.132',
    # 									user='rbdbusr',
    # 									password='Agl360UdmnB34Tz',
    # 									port=2499,
    # 									db='automation')

    # 	print("DB Connected")

    # except:

    # 	print("Can't connect to database")

    # # locations=[]
    # # with dbconnection1.cursor() as cursor:
    # # 		sql0 = "SELECT Target from ams_keyword_actionable_bid_param WHERE enabled_flag =1 group by 1 limit 1"
    # # 		cursor.execute(sql0)
    # # 		result0 = cursor.fetchall()
    # # 		a1=result0[0].replace("('",'').replace(")'",'')
    # # 		print(a1)
    # try:
    # 	html_container = driver.find_element_by_xpath('//*[@id="cm-app"]/div').get_attribute('innerHTML')
    # 	soup = BeautifulSoup(html_container, 'html.parser')
    # 	time.sleep(5)
    # except Exception as e:
    # 	print(e)

    # try:
    # 	print('im in try')
    # 	driver.find_element_by_xpath('//*[@id="targetingTab:targetingTab:quickFilter:input"]').send_keys('bike helmets for men')
    # 	time.sleep(20)
    # 	print('wjshnidiidhni')
    # 	# button.click()
    # except Exception as e:
    # 	print(e)
    # # Create an instance of tkinter frame
    # # win=Tk()

    # # # Set the geometry
    # # win.geometry("400x150")

    # # # Add a Scrollbar(horizontal)
    # # h=Scrollbar(win, orient='horizontal')
    # # h.pack(side=BOTTOM, fill='x')

    # try:
    # 	print('im in try')
    # 	driver.find_element_by_xpath('//*[@id="ag-634-input"]').click()
    # 	time.sleep(5)
    # 	print('wjshnidiidhni')
    # 	# button.click()
    # except Exception as e:
    # 	print(e)
    # try:
    # 	print('click on bid')
    # 	#bid=soup.find_element(By.CLASS_NAME, "cell-renderer-main-content-container currency-cell-renderer-main-content-container")

    # 	#bid=driver.find_element(By.CLASS_NAME, "cell-renderer-content-text")
    # 	myDiv = driver.find_element(By.CLASS_NAME, 'currency-cell-renderer-main-content-container')
    # 	bid = driver.find_element(By.CLASS_NAME, 'cell-renderer-content-text')
    # 	if bid.is_enabled():
    # 		print(bid.get_attribute("outerHTML"))
    # 		bid.click()
    # 		time.sleep(30)
    # 	else:
    # 		print(' not clicckkkkk')
    # 	# button.click()
    # except:
    # 	bid = driver.find_element(By.CLASS_NAME, 'cell-renderer-trigger currency-cell-renderer-trigger:hover')
    # 	bid.click()
    # 	print(' not clicckkkkk')
    # try:
    # 	print('im in try')
    # 	driver.find_element_by_xpath('//*[@id="targetingTab:table"]/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[4]/div/span/div/div[1]/div[1]/div[1]/div[2]').click()
    # 	time.sleep(10)
    # 	print('wjshnidiidhni')
    # 	# button.click()
    # except Exception as e:
    # 	print(e)
    # try:
    # 	print('im in try')
    # 	bid=driver.find_element_by_xpath('//*[@id="targetingTab:targetingTab:cell-bid-0:currencyEditorInput"]').click()
    # 	time.sleep(2)
    # 	bid=driver.find_element_by_xpath('//*[@id="targetingTab:targetingTab:cell-bid-0:currencyEditorInput"]').clear()
    # 	bid.send_keys('2.98')
    # 	time.sleep(2)
    # 	print('wjshnidiidhni')
    # 	# button.click()
    # except Exception as e:
    # 	print(e)
    # try:
    # 	print('im in try')
    # 	bid=driver.find_element_by_xpath('//*[@id="targetingTab:targetingTab:cell-bid-0:save"]').click()
    # 	bd=send_keys('2.98')
    # 	time.sleep(2)
    # 	print('wjshnidiidhni')
    # 	# button.click()
    # except Exception as e:
    # 	print(e)

    df1["report_type"] = "consolidated_creative_report"
    df1["created_on"] = datetime.datetime.now()
    df1["account"] = "vanish"

    cols = ",".join(list(df1.columns))

    insert_query = f" insert into flipkart_supermart_consolidated_creative_report_pca {cols} values(%s,%s,)"
