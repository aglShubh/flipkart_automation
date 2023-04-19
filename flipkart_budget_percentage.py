#!/usr/bin/env python
# coding: utf-8

"""Flipkart Campaign|AdGroup|Creative|FSN automation script."""

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
    filename = "Flipkart_budget_percentage_" + str(now) + ".log"
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
from selenium.webdriver.common.action_chains import ActionChains

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

curr_date = datetime.datetime.now()

flipkart_campaign_list = []


def getFlipkartCampaignData():
    cursor = db_connection.cursor()
    query = """SELECT campaign_id, campaign_status, campaign_budget_type, campaign_budget, platform_id, account_id FROM automation.flipkart_supermart_capaigns where campaign_id is not Null """
    cursor.execute(query=query)
    actionable_data = cursor.fetchall()

    for data in actionable_data:
        actionable_data_container = {}
        actionable_data_container["campaign_id"] = data["campaign_id"]
        actionable_data_container["campaign_status"] = data["campaign_status"]
        actionable_data_container["campaign_budget_type"] = data["campaign_budget_type"]
        actionable_data_container["campaign_budget"] = data["campaign_budget"]
        actionable_data_container["platform_id"] = data["platform_id"]
        actionable_data_container["account_id"] = data["account_id"]
        flipkart_campaign_list.append(actionable_data_container)

    return flipkart_campaign_list


print(getFlipkartCampaignData())


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


def getValueFromGraphBar():
    try:
        graph_bar = browser.find_element(
            By.XPATH,
            '//*[@id="list"]/div/div/div[2]/div/div/div/div/div/div[7]/div/div/span/div/progress',
        )
        val = float(graph_bar.get_attribute("value"))
        new_val = round(val, 2)
        print(val)
        # new_val = f"val : {val:.2f}"

    except Exception as _e:
        print(f"Error : {repr(_e)}")
    return new_val


def clickStatusFilterBox():
    try:
        status_box = browser.find_element(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]',
        )
        status_box.click()
        time.sleep(2)
        logger.info(f"status box clicked")
    except Exception as _e:
        logger.error(f"Error: click status filter box : {repr(_e)}")


def selectLiveFilter():
    try:
        live_box = browser.find_element(
            By.CSS_SELECTOR,
            "#popover-content > div > div.styles__CheckBoxContainer-sc-160a64n-3.dpmSdP > div:nth-child(1) > div > div > div > label",
        )
        live_box.click()
        time.sleep(2)
        logger.info(f"live status filter selected")
    except Exception as _e:
        logger.error(f"Error selecting filter item : {repr(_e)}")


def selectTotalBudgetMetFilter():
    try:
        total_budget_box = browser.find_element(
            By.CSS_SELECTOR,
            "#popover-content > div > div.styles__CheckBoxContainer-sc-160a64n-3.dpmSdP > div:nth-child(9) > div > div > div > label",
        )
        total_budget_box.click()
        time.sleep(2)
        logger.info(f"total budget met filter  selected")
    except Exception as _e:
        logger.error(f"Error selectong total budget met filter: {repr(_e)}")


def applyBtn():
    try:
        apply_btn = browser.find_element(
            By.XPATH, '//*[@id="popover-content"]/div/div[2]/button'
        )
        apply_btn.click()
        time.sleep(3)
        logger.info(f"filter applied")
    except Exception as _e:
        logger.error(f"Error click apply btn : {repr(_e)}")


def selectCampaignSearchBoxAndFilter(camp_id: str = ""):
    try:
        camp_filter_box = browser.find_element(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div/input',
        )
        camp_filter_box.click()
        time.sleep(2)
        logger.info(f"Campaign filter box click ")

        camp_filter_box.send_keys(camp_id)
        logger.info(f"camp id inserted: {camp_id}")
    except Exception as _e:
        logger.error(f"Error filtering campign : {repr(_e)}")


dttm = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")


def insertCrawlId():
    """Get max crawl id and insert next crawl id when script execute."""
    crawl_cursor = db_connection.cursor()
    crawl_cursor.execute(
        "select max(crawl_id) as mx from automation.flipkart_campaign_budget_spend;"
    )
    crawl_id = crawl_cursor.fetchone()
    crawl_id = crawl_id["mx"]
    print("line 378 ", crawl_id)
    print(type(crawl_id))

    if crawl_id is None:
        crawl_id = "1"
    else:

        crawl_id = int(crawl_id) + 1
        print(crawl_id)
        print(type(crawl_id))
    return crawl_id


crawl_id = insertCrawlId()
logger.info(f"crawl_id is {crawl_id}")


def getBudgetSpendPercentage():
    """Fun will get budget spend percentage and insert data into flipkart_campaign_budget_spend table."""
    for flip_camp in flipkart_campaign_list:
        campaign_id = flip_camp["campaign_id"]
        campaign_status = flip_camp["campaign_status"]
        campaign_budget_type = flip_camp["campaign_budget_type"]
        campaign_budget = flip_camp["campaign_budget"]
        platform_id = flip_camp["platform_id"]
        account_id = flip_camp["account_id"]

        # get the campaign based on account id and paltfrom id

        campaign_url = f"https://advertising.flipkart.com/ad-account/campaigns?baccount={account_id}&aaccount={platform_id}&ascending=false&dropDownVal=&searchString="
        browser.get(campaign_url)
        logger.info(
            f"campaign url open for account id {account_id} and platform id {platform_id}"
        )
        time.sleep(5)

        try:
            removePopUpBox()
            time.sleep(2)
            # clickStatusFilterBox()
            # time.sleep(2)
            # selectLiveFilter()
            # time.sleep(2)
            # selectTotalBudgetMetFilter()
            # time.sleep(2)
            # applyBtn()
            time.sleep(2)
            selectCampaignSearchBoxAndFilter(camp_id=campaign_id)
            time.sleep(10)
            percent_val = getValueFromGraphBar()
            print(percent_val)
            time.sleep(2)
            # insert data in flipkart_campaign_budget_spend
            try:
                query = """
                insert into flipkart_campaign_budget_spend (campaign_id, campaign_budget, campaign_status, budget_type, spend_percentage, crawl_id, created_at) values(%s,%s,%s,%s,%s,%s,%s)"""
                cursor = db_connection.cursor()
                cursor.execute(
                    query,
                    (
                        campaign_id,
                        campaign_budget,
                        campaign_status,
                        campaign_budget_type,
                        percent_val,
                        str(crawl_id),
                        curr_date,
                    ),
                )
                db_connection.commit()
                logger.info(f"data inserted for campaign id {campaign_id}")
            except Exception as _e:
                logger.error(f"Error inserting data for campaing id {campaign_id}")
        except Exception as _e:
            logger.error(f"Something went wrong : {repr(_e)}")
            pass


getBudgetSpendPercentage()
time.sleep(10)
