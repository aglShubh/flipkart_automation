#!/usr/bin/env python
# coding: utf-8

"""Flipkart Campaign amount/transctions history data."""

#######################################################################################################
# Futures

from asyncio.log import logger
import datetime
import logging

# Built-in/Generic Imports
import os
import sys
import time


# log file generating for each time script run
try:
    now = datetime.datetime.now()
    filename = "flipkart_campaign_transctions_history_" + str(now) + ".log"
    logging.basicConfig(
        filename=filename,
        filemode="w",
        format="%(asctime)s | %(levelname)s | %(message)s",
        level=logging.INFO,
    )

    execution_start_time = datetime.datetime.now()
    print(f"Execution start time : {execution_start_time}")
    logging.info(f"Script Execution start at : {execution_start_time}")
except Exception as e:
    logging.error(f"Error in creating log file : {repr(e)}")
    pass


import json

# Libs
import json
import sys
import csv
import requests
import pymysql

# third party module
try:
    # import awswrangler as wr  # to read from athena
    # import boto3
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import logging
    import re
    import pymysql.cursors
    from rich import print
    import datetime
    from iteration_utilities import unique_everseen


except Exception as e:
    print(f"Error in module import : {repr(e)}")
    logging.error(f"Module not found error : {repr(e)}")

# Own modules
# from {path} import {class}

#############################################################################################################

#############################################################################################################
# Owned
mj = "1"  # major
mn = "0"  # minor
pt = "0"  # patch
maintainer = "Shubham Jangid"
contact_email = "jangid.shubham@adglobal360.com"
dev_status = "dev"
python_version = sys.version
platform = f"Linux"
__author__ = f" AGL "
__copyright__ = f"Copyright 2022, AGL"
__credits__ = ["Shubham Jangid"]
__license__ = f"AGL PVT LIMITED"
__version__ = f"{mj}.{mn}.{pt}"
__maintainer__ = f"{maintainer}"
__email__ = f"{contact_email}"
__status__ = f"{dev_status}"

python_creater = """PyCon: “Code is more often read than written.” — Guido van Rossum"""

jeff = (
    """“Code tells you how; Comments tell you why.” — Jeff Atwood (aka Coding Horror)"""
)


logging.info(f"Module Description :  {__doc__}\n")
logging.info(f"{python_creater}")
logging.info(f"{jeff}\n")
logging.info(f"Python Version : {python_version}")
logging.info(f"Platform : {platform}")
logging.info(f"author : {__author__}")
logging.info(f"copyright : {__copyright__}")
logging.info(f"credits : {__credits__}")
# logging.info(f"Special thanks for help and support : {special_thanks}")
logging.info(f"license : {__license__}")
logging.info(f"version : {__version__}")
logging.info(f"maintainer : {__maintainer__}")
logging.info(f"contact_email : {__email__}")
logging.info(f"status : {__status__}\n")
print(f"Module Description :  {__doc__}")

############################################################################################################

# webdriver libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# creating instance for options
chrome_options = Options()
chrome_options.binary_location = (
    "/usr/bin/google-chrome"  # comment this line for headless mode
)
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument(
#     "--headless=new"
# )  # uncomment this line to run script in headleass mode
# chrome_options.headless = True

preferences = {
    "profile.default_content_settings.popups": 0,
    "download.default_directory": "/home/shubh/Desktop/AGL/chrome-headless/pcaPlaReports",
    "directory_upgrade": True,
}

chrome_options.add_experimental_option("prefs", preferences)
browser = webdriver.Chrome(
    executable_path="./drivers/chromedriver", options=chrome_options
)

# creating engine using sqlalchemy orm
from sqlalchemy import create_engine


def alchemy_connection():
    """Create connection using sqlalchemy."""
    engine = create_engine(
        "mysql+pymysql://rbuser:Agl325Umn1d@43.204.245.132:2499/automation"
    )
    return engine


# accounts and ids
vanish_platform_id: str = "C18XVZJB4GD7"
vanish_account_id: str = "RSAUFLMCSZ"

# configuration values
HOST = "43.204.245.132"
USERNAME = "rbdbusr"
PORT = 2499
PASSWORD = "Agl360UdmnB34Tz"
DATABASE_NAME = "automation"

# database connection
def database_connection():
    """Return connection for database."""
    try:
        connection = pymysql.connect(
            host=HOST,
            user=USERNAME,
            password=PASSWORD,
            port=PORT,
            db=DATABASE_NAME,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
    except pymysql.MySQLError as error:
        logging.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
        logging.error(error)
        print(f"Error : {error}")
    else:
        print(f"success")
        # logging.info("SUCCESS: Connection to RDS MySQL instance succeeded")
        return connection


db_connection = database_connection()


logger.info(f"Logging in ...")
login_url = "https://advertising.flipkart.com/login?tenant=BSS"


def logIn():
    """Login automation code for selenium."""
    browser.get(login_url)
    try:
        login_email_box = browser.find_element(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input',
        )
        login_email_box.click()
        login_email_box.send_keys("ebux.support@adglobal360.com")
        logger.info(f"Email inserted.")

        login_pass_box = browser.find_element(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/input',
        )
        login_pass_box.click()
        login_pass_box.send_keys("Ebuxsupport@@@@@@123")
        logger.info(f"Password inserted.")

        # click on login button
        login_btn = browser.find_element(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/form/div[3]/div[1]/button',
        )
        time.sleep(5)
        login_btn.click()
        time.sleep(5)
        logger.info(f"login button clicked.")

    except NoSuchElementException as _e:
        print(f"element not found {repr(_e)}")
    except Exception as _e:
        print(f"Error finding element or sending keys {repr(_e)}")
    else:
        logger.info(f"logged in successfully.")


logIn()
time.sleep(5)

wallet_summary_url = f"https://advertising.flipkart.com/ad-account/wallet/summary?baccount=RSAUFLMCSZ&aaccount=C18XVZJB4GD7"
browser.get(wallet_summary_url)
time.sleep(5)


def removePopUpBox() -> None:
    try:
        pop_box = browser.find_element(
            By.XPATH, '//*[@id="popover-content"]/div/div/div[2]/button'
        )
        pop_box.click()
        time.sleep(2)
        logger.info(f"pop up box removed..")
    except Exception as _e:
        logger.error(f"Error removing pop up box")
        pass


removePopUpBox()
time.sleep(2)


def getAvailableBalance():
    try:
        avail_balance = browser.find_element(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div',
        )
        avail_balance = avail_balance.get_attribute("innerText")
        print(avail_balance)
        logger.info(f"available balance is : {avail_balance}")
    except Exception as _e:
        logger.error(f"Error getting available balance... {repr(_e)}")

    return avail_balance


_balance = getAvailableBalance()
print("_balance", _balance)

dttm = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")


def getTransctionHistory():
    wallet_data = requests.get(wallet_summary_url).text
    time.sleep(50)

    # scroll the bar to get all data
    # SCROLL_PAUSE_TIME = 5
    # last_height = browser.execute_script("return document.body.scrollHeight")
    # while True:
    #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(SCROLL_PAUSE_TIME)
    #     new_height = browser.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         break
    #     last_height = new_height
    # time.sleep(2)

    # last_height = browser.execute_script("return document.body.scrollHeight")
    # print(last_height)

    # Scroll down to bottom
    # y = 1200
    # finished = False
    # while True:
    #     for timer in range(0, 100):
    #         browser.execute_script("window.scrollTo(0, " + str(y) + ")")
    #         y += 1200
    #         time.sleep(10)
    #         new_height = browser.execute_script("return document.body.scrollHeight")
    #         print(new_height, last_height)

    #         if new_height == last_height: #on the first iteration new_height equals last_height
    #             print('stop')
    #             finished = True
    #             break
    #         last_height = new_height
    #     if finished:
    #         break

    # browser.execute_script("window.scrollTo(0, 350);")
    # time.sleep(5)

    loc_html = browser.find_element(
        By.XPATH,
        '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div',
    ).get_attribute("innerHTML")
    _soup = BeautifulSoup(loc_html, "html.parser")

    # find the main div which contains transctional history data
    trans_data = _soup.findAll("div", {"class": "styles-sc-1w9jjyu-1 jTGVnL"})
    logger.info(f"len of data : {len(trans_data)}")

    transaction_details_list = []

    for data in trans_data:
        transaction_details = {}

        items = [
            item.text
            for item in data.find_all(
                "div", {"class": "styles__TableColumn-nbhc5i-3 bFpDvQ"}
            )
        ]

        transaction_details["transaction_details"] = items[0]
        transaction_details["update_on"] = items[1]
        transaction_details["status"] = items[2]
        transaction_details["available_balance"] = _balance
        transaction_details["amount"] = data.find("span", {"class": "amount"}).text
        transaction_details["datetime"] = dttm
        transaction_details_list.append(transaction_details)

    return transaction_details_list


# getTransctionHistory()
# time.sleep(15)


def insertInToTable():
    val = getTransctionHistory()
    cursor = db_connection.cursor()

    try:
        query = """insert into automation.flipkart_campaign_transctions_history 
            (transaction_details, updated_on, available_balance, amount, status, created_at) 
            values(%(transaction_details)s,%(update_on)s,%(available_balance)s,%(amount)s,%(status)s,%(datetime)s)"""
        cursor.executemany(query, val)
        logger.info(f"data  {len(val)} rows inserted.")
    except Exception as _e:
        logger.error(f"Error inserting data : {repr(_e)}")

    db_connection.commit()


# final call


insertInToTable()
