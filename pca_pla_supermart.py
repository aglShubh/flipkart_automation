#!/usr/bin/env python
# coding: utf-8

"""Flipkart PCA/PLA Supermart reports download module."""

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
    filename = "Flipkart_PCA_PLA" + str(now) + ".log"
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

    # from rich import print
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
chrome_options.binary_location = "/usr/bin/google-chrome"
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument('--headless=new')
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


account : str = "4YILERKLSZ92"


# configuration values
HOST = "43.204.245.132"
USERNAME = "rbdbusr"
PORT = 2499
PASSWORD = "Agl360UdmnB34Tz"
DATABASE_NAME = "automation"

# # database connection
# def database_connection():
#     """Return connection for database."""
#     try:
#         connection = pymysql.connect(
#             host=HOST,
#             user=USERNAME,
#             password=PASSWORD,
#             port=PORT,
#             db=DATABASE_NAME,
#             charset="utf8mb4",
#             cursorclass=pymysql.cursors.DictCursor,
#         )
#     except pymysql.MySQLError as error:
#         logging.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
#         logging.error(error)
#         print(f"Error : {error}")
#     else:
#         print(f"success")
#         # logging.info("SUCCESS: Connection to RDS MySQL instance succeeded")
#         return connection

# db_connection = database_connection()


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

pca_url = f"https://advertising.flipkart.com/ad-account/reports/pca?baccount=RSAUFLMCSZ&aaccount={account}"
pla_url = f"https://advertising.flipkart.com/ad-account/reports/pla?baccount=RSAUFLMCSZ&aaccount={account}"


def removePopUpBox(url: str = None) -> None:
    if url != None:
        browser.get(url=url)
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


def clickAccountDropDown():
    try:
        account_dd = browser.find_element(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[1]/div/div[1]/div[3]/div[5]/div/span[2]',
        )
        account_dd.click()
        time.sleep(3)
        logger.info(f"account dropdown clicked")
    except Exception as _e:
        logger.error(f"Error clicking account dropdown {repr(_e)}")


def selectAccount():
    try:
        choose_account = browser.find_element(
            By.XPATH, '//*[@id="popover-content"]/div/div[1]/div[2]/a[3]/div/div'
        )
        choose_account.click()
        time.sleep(3)
        logger.info(f"Account selected Mars")
    except Exception as _e:
        logger.info(f"Error selecting account {repr(_e)}")


def clickDropDown():
    try:
        time.sleep(3)
        drop_down = browser.find_element(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div',
        )
        drop_down.click()
        logger.info(f"drop down clicked")
        time.sleep(3)
    except Exception as _e:
        logger.error(f"Error : {repr(_e)}")


def selectSuperMart():
    try:
        select_super_mart = browser.find_element(
            By.XPATH, '//*[@id="popover-content"]/div/div[2]'
        )
        select_super_mart.click()
        time.sleep(3)
        logger.info(f"supermart option selected...")
    except Exception as _e:
        logger.info(f"Error : {repr(_e)}")


def clickDateRange():
    try:
        date_box = browser.find_element(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div',
        )
        date_box.click()
        logger.info(f"date box clicked")
        time.sleep(3)
        date_range = browser.find_element(
            By.XPATH, '//*[@id="popover-content"]/div/div[1]/div[2]'
        )
        date_range.click()
        logger.info(f"Date range selected")
    except Exception as _e:
        logger.error(f"Error selecting date {repr(_e)}")


def downloadReport():
    try:
        time.sleep(3)
        download_report = browser.find_element(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[4]/div[2]/div/span/div',
        )
        download_report.click()
        time.sleep(5)
        logger.info(f"Download btn clicked! Report downloaded")
    except Exception as _e:
        logger.error(f"Error downloading report {repr(_e)}")


def renameDownloadFile():

    rootdir = "/home/shubh/Desktop/AGL/chrome-headless/pcaPlaReports/"
    regex = re.compile("(.*csv$)")

    for root, dirs, files in os.walk(rootdir):
        for file in files:
            if regex.match(file):
                logger.info(f"Downloaded file name : {file}")
                old_name = (
                    f"/home/shubh/Desktop/AGL/chrome-headless/pcaPlaReports/{file}"
                )
                new_name = f"/home/shubh/Desktop/AGL/chrome-headless/pcaPlaReports/downloaded.csv"
                logger.info(f"changed file name : {new_name}")
                os.rename(old_name, new_name)
                logger.info(f"file name changed..")


def changeCSVColumn(report_type: str = "", campaign_type: str = "") -> None:

    df = pd.read_csv(
        r"/home/shubh/Desktop/AGL/chrome-headless/pcaPlaReports/downloaded.csv",
        skiprows=4,
    )
    df1 = pd.DataFrame(df)
    df1["report_type"] = report_type  # name change
    df1["created_on"] = datetime.datetime.today() - datetime.timedelta(days=1)
    df1["account"] = "Brand 1"
    df1["platform"] = "SM"

    if campaign_type == "pca":
        df2 = df1.rename(
            columns={
                "Campaign Budget Type": "campaign_budget_type",
                "Direct ROI": "direct_roi",
                "Indirect ROI": "indirect_roi",
            }
        )
    elif campaign_type == "pla":
        df2 = df1.rename(
            columns={
                "Campaign ID": "campaign_id",
                "Campaign Name": "campaign_name",
                "Ad Spend": "ad_spend",
                "Add to Baskets": "add_to_baskets",
                "Add to Basket Rate": "add_to_basket_rate",
                "Units Sold (Direct)": "units_sold_direct",
                "Units Sold (Indirect)": "units_sold_indirect",
                "Direct Revenue": "direct_revenue",
                "Indirect Revenue": "indirect_revenue",
                "ROI (Direct)": "roi_direct",
                "ROI (Indirect)": "roi_indirect",
            }
        )

    return df2


def insertDataIntoDB(df2: pd.DataFrame = "", table_name: str = ""):

    df2.to_sql(
        name=table_name,  # table name
        con=alchemy_connection(),
        if_exists="append",
        index=False,
    )
    logger.info("inserting data...")


def removeLastDownloadedFile(path: str = "") -> None:
    import glob

    files = glob.glob(path)
    for f in files:
        os.remove(f)
    logger.info(f"file removed..")


# flipkart_supermart_pca_campaign
def flipkartSupermartPcaCampaign():
    time.sleep(3)
    clickAccountDropDown()
    time.sleep(3)
    selectAccount()
    time.sleep(3)
    removePopUpBox(url=None)
    time.sleep(3)
    removePopUpBox(url=pca_url)
    time.sleep(3)
    clickDropDown()
    time.sleep(2)
    selectSuperMart()
    time.sleep(3)
    clickDateRange()
    time.sleep(3)
    downloadReport()
    time.sleep(5)
    renameDownloadFile()
    time.sleep(3)
    insertDataIntoDB(
        df2=changeCSVColumn(report_type="campaign_report", campaign_type="pca"),
        table_name="flipkart_supermart_pca_campaign",
    )
    time.sleep(10)
    removeLastDownloadedFile(
        path="/home/shubh/Desktop/AGL/chrome-headless/pcaPlaReports/*"
    )
    time.sleep(2)


logger.info(f"Report downloading and inserting data for supermart pca campaign")
flipkartSupermartPcaCampaign()
logger.info(f"done for PCA")

# flipkart_supermart_pla_campaign
def flipkartSupermartPlaCampaign():
    time.sleep(3)
    clickAccountDropDown()
    time.sleep(3)
    selectAccount()
    time.sleep(3)
    removePopUpBox(url=None)
    time.sleep(3)
    removePopUpBox(url=pla_url)
    time.sleep(3)
    clickDropDown()
    time.sleep(2)
    selectSuperMart()
    time.sleep(3)
    clickDateRange()
    time.sleep(3)
    downloadReport()
    time.sleep(5)
    renameDownloadFile()
    time.sleep(3)
    insertDataIntoDB(
        df2=changeCSVColumn(report_type="campaign_report", campaign_type="pla"),
        table_name="flipkart_supermart_pla_campaign",
    )
    time.sleep(10)
    removeLastDownloadedFile(
        path="/home/shubh/Desktop/AGL/chrome-headless/pcaPlaReports/*"
    )
    time.sleep(2)


logger.info(f"Report downloading and inserting data for supermart pla campaign")
flipkartSupermartPlaCampaign()
logger.info(f"done for PLA")

time.sleep(3)
browser.quit()
logger.info(f"Browser Exit..")
