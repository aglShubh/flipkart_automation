#!/usr/bin/env python
# coding: utf-8

"""Flipkart Campaign set bit PLA automation script."""

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
    filename = "Flipkart_Set_bid_PCA" + str(now) + ".log"
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
import pandas as pd
import csv
import requests
import pymysql

# third party module
try:
    # import awswrangler as wr  # to read from athena
    # import boto3
    import requests
    import sys
    import pandas as pd
    import logging
    import time
    import re
    import pymysql.cursors
    from rich import print
    import pandas as pd
    import datetime
    import time
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
# chrome_options.add_argument('--headless=new') # uncomment this line to run script in headleass mode
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
    engine = create_engine(
        "mysql+pymysql://rbuser:Agl325Umn1d@43.204.245.132:2499/automation"
    )
    return engine

mars_account : str = "4YILERKLSZ92"
vanish_account : str = "C18XVZJB4GD7"

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

# camp_url : str = "https://advertising.flipkart.com/ad-account/campaigns?baccount=RSAUFLMCSZ&aaccount=C18XVZJB4GD7"



actionalble_data_list = []
def getActionableData():
    cursor = db_connection.cursor()
    query = """SELECT action_status, segment, action_type, action, fsn_id, campaign_id, ad_group_id, set_value FROM automation.rpa_action where action_status = 1;"""
    cursor.execute(query=query)
    actionable_data = cursor.fetchall()

    for data in actionable_data:
        actionable_data_container = {}
        actionable_data_container["action_status"] = data["action_status"]
        actionable_data_container["segment"] = data["segment"]
        actionable_data_container["action_type"] = data["action_type"]
        actionable_data_container["action"] = data["action"]
        actionable_data_container["fsn_id"] = data["fsn_id"]
        actionable_data_container["campaign_id"] = data["campaign_id"]
        actionable_data_container["ad_group_id"] = data["ad_group_id"]
        actionable_data_container["set_value"] = data["set_value"]
        actionalble_data_list.append(actionable_data_container)

    return actionalble_data_list

print(getActionableData())


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


def clickContinue():
    try:
        con = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/button[2]')
        con.click()
        time.sleep(3)
        logger.info(f"continue btn clicked")
    except Exception as _e:
        logger.error(f"Error clicking cont btn {repr(_e)}")



def bidBoxPCA(set_val = None, path : str = None):
    try:
        bid_box = browser.find_element(By.XPATH, path)
        bid_box.click()
        time.sleep(3)
        bid_box.click()
        val: any = bid_box.get_attribute("value")
        logger.info(f"current val of bid is : {val}")
        bid_box.send_keys(Keys.CONTROL + "a")
        bid_box.send_keys(Keys.DELETE)
        time.sleep(2)
        bid_box.send_keys(set_val)
        logger.info(f"New bid value : {set_val}")
    except Exception as _e:
        logger.error(f"Error in set bid for pla campaign.. {repr(_e)}")

def nextBtn(path:str = None):
    try:
        btn = browser.find_element(By.XPATH, path)
        btn.click()
        time.sleep(2)
        logger.info(f"next btn click...")
    except Exception as _e:
        logger.info(f"Error clicking on next btn {repr(_e)}")

def saveAdGroup():
    try:
        btn = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[4]/div/div[2]/div/div[7]/button[2]')
        btn.click()
        time.sleep(2)
        logger.info(f"save ad group  btn click...")
    except Exception as _e:
        logger.info(f"Error clicking on save ad group btn {repr(_e)}")


def finalContinueBtn():
    try:
        con = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/button[2]')
        con.click()
        time.sleep(3)
        logger.info(f"final continue btn clicked")
    except Exception as _e:
        logger.error(f"Error clicking cont btn {repr(_e)}")

def submit(path:str = None):
    try:
        con = browser.find_element(By.XPATH, path)
        con.click()
        time.sleep(3)
        logger.info(f"submit btn clicked")
    except Exception as _e:
        logger.error(f"Error clicking submit btn {repr(_e)}")


def setOrUpdateBid():
    for camp in actionalble_data_list:
        campaign_id = camp["campaign_id"]
        ad_group_id = camp["ad_group_id"]
        set_value = camp["set_value"]
        action = camp["action"]
        seg = camp["segment"]
        print(action)
        if action == "set_bid" and seg == "pca":
            bid_url = f"https://advertising.flipkart.com/ad-account/campaigns/{seg.lower()}/{campaign_id}/edit?baccount=RSAUFLMCSZ&aaccount={vanish_account}&adgroupid={ad_group_id}&substep=1"
            browser.get(bid_url)
            time.sleep(3)
            removePopUpBox()
            time.sleep(3)
            removePopUpBox()
            time.sleep(3)
            clickContinue()
            time.sleep(3)
            nextBtn(path = '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/button[2]')
            time.sleep(3)
            nextBtn(path='//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[3]/div/div[2]/div/div[2]/button[2]')
            time.sleep(3)
            bidBoxPCA(set_val=set_value,path='//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[4]/div/div[2]/div/div[4]/div/div[1]/div[2]/div/input')
            time.sleep(2)
            saveAdGroup()
            time.sleep(3)
            finalContinueBtn()
            time.sleep(3)
            submit(path = '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/button[2]')
            time.sleep(5)


setOrUpdateBid()
time.sleep(5)
browser.quit()

# marsh acccount add.
# problem in pca submit#################