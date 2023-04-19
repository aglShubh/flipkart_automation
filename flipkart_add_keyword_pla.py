#!/usr/bin/env python
# coding: utf-8

"""Flipkart Add fsn for PLA."""

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
    filename = "flipkart_add_keyword_pla" + str(now) + ".log"
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

actionalble_data_list = []


def getActionableData():
    cursor = db_connection.cursor()
    query = """SELECT action_status, segment, action_type, action, fsn_id, campaign_id, ad_group_id, set_value, platform_id, account_id FROM automation.rpa_action where action_status = 1 and id= 92;"""
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
        actionable_data_container["platform_id"] = data["platform_id"]
        actionable_data_container["account_id"] = data["account_id"]
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


def clickAdKeyword():
    try:
        add_keyword = browser.find_element(
            By.CSS_SELECTOR,
            "#app > div:nth-child(1) > div:nth-child(1) > div > div.content > div > div.styles__StyledPlayArea-ihipf8-1.eGKFPt > div.styles__FormContainer-crkiwy-0.cTJTVe > div.styles__Container-sc-10vyvdr-0.idyeIu > div.styles__StepContentContainer-sc-10vyvdr-6.bZNeer > div:nth-child(6) > div.styles__AdGroupTable-j5kc28-32.jKIvJa > table > tbody > tr:nth-child(2) > td:nth-child(4) > div > a",
        )
        add_keyword.click()
        logger.info(f"add keyword click...")
        time.sleep(3)
    except Exception as _e:
        logger.error(f"Error clicking ad keyword link .. {repr(_e)}")


x = "https://advertising.flipkart.com/ad-account/campaigns/pla/0K2C8GAF2NIE/edit?baccount=RSAUFLMCSZ&aaccount=C18XVZJB4GD7&step=1"
browser.get(x)
time.sleep(7)


def selectAndClickAdKeyword():
    try:
        ex_keyword = browser.find_element(
            By.CSS_SELECTOR,
            "#app > div:nth-child(1) > div:nth-child(1) > div > div.content > div > div.styles__StyledPlayArea-ihipf8-1.eGKFPt > div.styles__FormContainer-crkiwy-0.cTJTVe > div.styles__Container-sc-10vyvdr-0.idyeIu > div.styles__StepContentContainer-sc-10vyvdr-6.bZNeer > div:nth-child(6) > div.styles__AdGroupTable-j5kc28-32.jKIvJa > table > tbody > tr:nth-child(2) > td:nth-child(4) > div > section > div:nth-child(2) > svg",
        )
        ex_keyword.click()
        time.sleep(3)
        logger.info(f"add keyword click...")
    except Exception as _e:
        logger.error(f"Error clicking ad keyword link .. {repr(_e)}")


selectAndClickAdKeyword()


def continueBtn(path: str = ""):
    try:
        c_btn = browser.find_element(
            By.XPATH,
            path,
        )
        c_btn.click()
        time.sleep(3)
        logger.info(f"conitnue btn clicked...")
    except Exception as _e:
        logger.error(f"Error clicking cnt btn... {repr(_e)}")


def submit(path: str = None):
    try:
        con = browser.find_element(By.XPATH, path)
        con.click()
        time.sleep(3)
        logger.info(f"submit btn clicked")
    except Exception as _e:
        logger.error(f"Error clicking submit btn {repr(_e)}")


def createFsnPlaCsv(exact_keyword: str = "", broad_keyword: str = ""):
    exact_pla_keyword = exact_keyword.split(",")
    print(exact_pla_keyword)
    broad_pla_keyword = broad_keyword.split(",")
    print(broad_pla_keyword)

    # to remove the rows
    df = pd.read_csv("addKeywordPla/pla_keyword.csv")
    index = list(range(1, df.shape[0]))
    df.drop(index, axis=0, inplace=True)
    df.to_csv("addKeywordPla/pla_keyword.csv", index=False)
    print(df)
    time.sleep(3)

    # df1 = pd.DataFrame(exact_pla_keyword,broad_pla_keyword)
    # print(df1)
    # df1.to_csv("addKeywordPla/pla_keyword.csv", mode="a", index=False, header=False)
    # time.sleep(3)


createFsnPlaCsv(exact_keyword="a,b,c,d")

# write on csv then upload
def uploadFsnProduct():
    try:
        time.sleep(3)
        upload_box = browser.find_element(
            By.XPATH,
            '//*[@id="app"]/div[2]/div[4]/aside/section/div[1]/div[2]/div/div/div[2]/div[5]/div[1]',
        )
        time.sleep(3)
        logger.info(f"upload product csv box clicked")

        # upload file
        elm = browser.find_element(By.XPATH, "//input[@type='file']")
        # need to change the path in main function
        try:
            elm.send_keys(os.getcwd() + "/addKeywordPla/pla_keyword.csv")
            time.sleep(3)
        except:
            os.mkdir("addKeywordPla")
            elm.send_keys(os.getcwd() + "/addKeywordPla/pla_keyword.csv")
            time.sleep(3)

        logger.info(f"file uploaded")
        time.sleep(3)
    except Exception as _e:
        logger.error(f"Error uploading csv product fsn file {repr(_e)}")


def addKeywordPla():
    for act in actionalble_data_list:
        account_id = act["account_id"]
        platform_id = act["platform_id"]
        campaign_id = act["campaign_id"]
        ad_group_id = act["ad_group_id"]
        segment = act["segment"]
        fsn_id = act["fsn_id"]
        action = act["action"]

        if action == "add_keyword" and segment.lower() == "pla":
            pla_keyword_edit_url = f"https://advertising.flipkart.com/ad-account/campaigns/{segment.lower()}/{campaign_id}/edit?baccount={account_id}&aaccount={platform_id}&step=1"
            browser.get(pla_keyword_edit_url)
            time.sleep(5)
            try:
                removePopUpBox()
                time.sleep(2)
                createFsnPlaCsv(fsn_ids=fsn_id)
                time.sleep(3)
                uploadFsnProduct()
                time.sleep(3)
                continueBtn(
                    path='//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/button[2]'
                )
                time.sleep(2)
                removePopUpBox()
                time.sleep(2)
                continueBtn(
                    path='//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/button[2]'
                )
                time.sleep(3)
                removePopUpBox()
                time.sleep(2)
                submit(
                    path='//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/button[2]'
                )
                time.sleep(2)

            except Exception as _e:
                logger.error(f"something went wrong at final stage : {repr(_e)}")


# addKeywordPla()
logger.info(f"Fsn successfully added...")
time.sleep(5)
browser.quit()
