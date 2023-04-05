#!/usr/bin/env python
# coding: utf-8

"""Flipkart Create campaign automation script."""

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
    filename = "Create_campaign_pla" + str(now) + ".log"
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
mars_account: str = "C18XVZJB4GD7"
vanish_account: str = "C18XVZJB4GD7"

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


campaign_data_list = []


def getDataForCampaignCreation():
    """Get data from ebux_campaign table to create campaign."""
    cursor = db_connection.cursor()
    query = """SELECT campaign_name,
        platform, 
        brand, 
        category, 
        products,
        businesszone,
        cost_model, 
        start_duration,
        end_duration,
        is_till_end_duration, 
        campaign_budget, 
        cost_per_basket,
        budget_limit, 
        FSNs,
        keywords_broad,
        keywords_exact,
        top_of_search_page, 
        rest_of_search_page, 
        top_of_browse_page, 
        rest_of_browse_page, 
        budget_type,
        exclude_keywords,
        segment, 
        campaign_status FROM ebux_campaign where campaign_status = 1 and campaign_name = 'etwetwer'"""
    cursor.execute(query=query)
    campaign_data = cursor.fetchall()

    for data in campaign_data:
        campaign_data_container = {}
        campaign_data_container["campaign_name"] = data["campaign_name"]
        campaign_data_container["platform"] = data["platform"]
        campaign_data_container["brand"] = data["brand"]
        campaign_data_container["category"] = data["category"]
        campaign_data_container["products"] = data["products"]
        campaign_data_container["businesszone"] = data["businesszone"]
        campaign_data_container["cost_model"] = data["cost_model"]
        campaign_data_container["start_duration"] = data["start_duration"]
        campaign_data_container["end_duration"] = data["end_duration"]
        campaign_data_container["is_till_end_duration"] = data["is_till_end_duration"]
        campaign_data_container["campaign_budget"] = data["campaign_budget"]
        campaign_data_container["cost_per_basket"] = data["cost_per_basket"]
        campaign_data_container["budget_limit"] = data["budget_limit"]
        campaign_data_container["FSNs"] = data["FSNs"]
        campaign_data_container["keywords_broad"] = data["keywords_broad"]
        campaign_data_container["keywords_exact"] = data["keywords_exact"]
        campaign_data_container["top_of_search_page"] = data["top_of_search_page"]
        campaign_data_container["rest_of_search_page"] = data["rest_of_search_page"]
        campaign_data_container["top_of_browse_page"] = data["top_of_browse_page"]
        campaign_data_container["rest_of_browse_page"] = data["rest_of_browse_page"]
        campaign_data_container["budget_type"] = data["budget_type"]
        campaign_data_container["exclude_keywords"] = data["exclude_keywords"]
        campaign_data_container["segment"] = data["segment"]
        campaign_data_container["campaign_status"] = data["campaign_status"]

        campaign_data_list.append(campaign_data_container)

    return campaign_data_list

print(getDataForCampaignCreation())

camp_page_url = f"https://advertising.flipkart.com/ad-account/campaigns?baccount=RSAUFLMCSZ&aaccount=C18XVZJB4GD7"
browser.get(camp_page_url)
time.sleep(3)

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


def selectCreateCampaign():
    try:
        cc = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div/button')
        cc.click()
        time.sleep(3)
        logger.info(f"Create campaign btn clicked...")
    except Exception as _e:
        logger.error(f"Error clicking create campaign btn... {repr(_e)}")

selectCreateCampaign()

def selectCampaignType(campaign_path :str = ""):
    try:
        # //*[@id="app"]/div[2]/div[7]/div/div[2]/div/div[2]/div/a[1] # pla only
        # //*[@id="app"]/div[2]/div[7]/div/div[2]/div/div[2]/div/a[2]
        pla_camp = browser.find_element(By.XPATH, campaign_path)
        pla_camp.click()
        time.sleep(3)
        logger.info(f"campaign option selected")
    except Exception as _e:
        logger.error(f"Error selecting option {repr(_e)}")

selectCampaignType(campaign_path='//*[@id="app"]/div[2]/div[7]/div/div[2]/div/div[2]/div/a[1]')

def selectAndEnterCampaignName(camp_name:str = ""):
    try:
        camp_box = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div/div[2]/div/input')
        camp_box.click()
        logger.info(f"Input box clicked and focused")
        time.sleep(2)
        camp_box.send_keys(camp_name)
        logger.info(f"campaign name inserted {camp_name}")
    except Exception as _e:
        logger.error(f"Error something went wrong ... {repr(_e)}")

selectAndEnterCampaignName(camp_name="test camp")

def selectAdPlatform(platform_path:str = ""):
    try:
        # flipkart : //*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div[1]/div
        # sm : //*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div[2]/div
        select_option = browser.find_element(By.XPATH, platform_path)
        select_option.click()
        time.sleep(3)
        logger.info(f"ad platfrom selected...")
    except Exception as _e:
        logger.error(f"Error selecting ad platform..{repr(_e)}")

selectAdPlatform(platform_path='//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div[1]/div')

def continueBtn():
    try:
        c_btn = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/button[3]')
        c_btn.click()
        time.sleep(3)
        logger.info(f"conitnue btn clicked...")
    except Exception as _e:
        logger.error(f"Error clicking cnt btn... {repr(_e)}")

# continueBtn()

# write on csv then upload
def uploadFsnProduct():
    try:
        time.sleep(3)
        upload_box = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/div[1]')
        time.sleep(3)
        logger.info(f"upload product csv box clicked")
        
        # upload file 
        elm = browser.find_element(By.XPATH, "//input[@type='file']")
        # need to change the path in main function
        elm.send_keys(os.getcwd() + "/fsnProductCSV/pla_fsn.csv")
        logger.info(f"file uploaded")
        time.sleep(3)
    except Exception as _e:
        logger.error(f"Error uploading csv product fsn file {repr(_e)}")

uploadFsnProduct()
continueBtn()
time.sleep(5)

def setDate():
    try:
        cal_icon_box = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div/div/div/div/input')
        cal_icon_box.click()
        time.sleep(2)
        logger.info(f"calender box clicked")

        set_date = browser.find_element(By.XPATH, '//*[@id="popover-content"]/div')
        # set_date.click()
        # set_date.send_keys("08")
        browser.execute_script("arguments[0].value = '05/04/2023 08:10'", setDate)
        logger.info(f"date set ")
    except Exception as _e:
        logger.error(f"Error setting new date : {repr(_e)}")

setDate()                               
time.sleep(30)

def setStartEndTime():
    try:
        set_time_box = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div/div/div/div/input')
        # set_time_box.click()
        time.sleep(3)

        logger.info(f"set start time..")
        yr = '2023'
        mn = '4'
        dt = '3'
        # set_time_box.clear()
        # print("here")
        # set_time_box.send_keys(Keys.CONTROL + "a")
        # print("here")
        # set_time_box.send_keys(Keys.DELETE)
        # print("here")
        try:
            # set_time_box.click()
            # cal_box = browser.find_element(By.XPATH, '//*[@id="popover-content"]/div')
            browser.execute_script("arguments[0].value = '05/04/2023 08:10'", set_time_box)
            # set_time_box.send_keys('04/04/2023')
            # time.sleep(4)
            # set_time_box.send_keys(Keys.ENTER)
            print("now here")
        except Exception as _e:
            print(f"error {repr(_e)}")
        # set_time_box.click()
        # cc = browser.find_element(By.XPATH, '//*[@id="popover-content"]/div/div[1]')
        # cc.send_keys('04/04/2023')
        # print("setttt")
    except Exception as _e:
        logger.error(f"Error setting up date.. {repr(_e)}")

# setStartEndTime()
# time.sleep(300)


def setBudget():
    try:
        budget_box = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[4]/div/div/div/input')
        budget_box.click()
        time.sleep(2)
        budget_box.send_keys("1000")
        logger.info(f"budget value set ")
    except Exception as _e:
        logger.error(f"Error setting budget {repr(_e)}")

# time.sleep(3)
# setBudget()
# time.sleep(2)
# setStartEndTime()
# time.sleep(90)


def createCampaign():
    """Campaign creating automation function."""
    pass
