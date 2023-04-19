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
    filename = "Flipkart_Campaign" + str(now) + ".log"
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


# account : str = "4YILERKLSZ92" #
account = "C18XVZJB4GD7"  # vanish

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
    query = """SELECT action_status, segment, action_type, action, fsn_id, campaign_id, ad_group_id FROM automation.rpa_action where action_status = 0 and action in ("enable","pause") limit 5;"""
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


def searchAndGetCampaignStatus(search_url: str = ""):
    search_url = search_url
    browser.get(search_url)
    time.sleep(3)
    removePopUpBox()
    time.sleep(2)

    # get campaign status
    try:
        time.sleep(2)
        state = browser.find_element(
            By.CSS_SELECTOR,
            "#list > div > div > div:nth-child(2) > div > div > div > div > div > div:nth-child(2) > div > div > span.styles__StyledCampaignStatus-lju9ke-4.pfLcH > div > span",
        )
        state.click()
        state_val = state.get_attribute("innerText")
        logger.info(f"state value is : {state_val}")
        return state_val
    except Exception as _e:
        logger.error(f"Error gettting status value of campaign: {repr(_e)}")


def changePcaPlaCampaignState():
    """Enable and pause the camapign."""
    for camp in actionalble_data_list:
        campaign_id = camp["campaign_id"]
        ad_group_id = camp["ad_group_id"]
        action = camp["action"]
        seg = camp["segment"]

        search_campaign_url = f"https://advertising.flipkart.com/ad-account/campaigns?baccount=RSAUFLMCSZ&aaccount={account}&ascending=false&searchString={campaign_id}"

        campaign_exact_status = searchAndGetCampaignStatus(
            search_url=search_campaign_url
        )
        logger.info(f"cmapaign {campaign_id} status is {campaign_exact_status.lower()}")
        logger.info(f"campaing {campaign_id} db status is {action.lower()}")

        # action param need to change in db as live and paused
        if campaign_exact_status.lower() == "completed":
            logger.info(f"campaign status completed passed..")
            pass
        elif campaign_exact_status.lower() == "aborted":
            logger.info(f"campaign status is aborted so passed")
            pass
        elif action.lower() == campaign_exact_status.lower():
            logger.info(
                f"pass as {action.lower()} and {campaign_exact_status.lower()} matched"
            )
            pass
        else:
            camp_url = f"https://advertising.flipkart.com/ad-account/campaigns/{seg.lower()}/{campaign_id}?baccount=RSAUFLMCSZ&aaccount={account}"
            browser.get(camp_url)
            print(f"I am here {camp_url}")
            time.sleep(3)
            logger.info(
                f"Segment {camp['segment']} and campaign_id {campaign_id} selected."
            )
            try:
                removePopUpBox()
                time.sleep(3)
                logger.info(f"Pop up box removed...")
            except Exception as _e:
                removePopUpBox()
                logger.error(f"Not removed error {repr(_e)}")
                pass
            try:
                # change state block
                time.sleep(5)
                r_path = browser.find_element(
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/header/section/div[2]/div/span[3]/div',
                )
                r_path.click()
                logger.info(f"campaign state changed successfully")
                time.sleep(3)
                cursor = db_connection.cursor()
                q = """update  automation.rpa_action set action_status = 0 where campaign_id = %s and ad_group_id = %s"""
                cursor.execute(q, (campaign_id, ad_group_id))
                db_connection.commit()
                logger.info(f"Action status changed...")

            except Exception as _e:
                logger.error(
                    f"Error changing state of campaign or no such box to click{repr(_e)}"
                )
                pass
            time.sleep(5)


changePcaPlaCampaignState()
time.sleep(10)
browser.quit()
