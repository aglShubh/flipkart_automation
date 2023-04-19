#!/usr/bin/env python
# coding: utf-8

"""Flipkart PLA reports download module."""

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
    filename = "Flipkart_Reports_PLA" + str(now) + ".log"
    logging.basicConfig(
        filename=filename,
        filemode="w",
        format="%(asctime)s | %(levelname)s | %(message)s",
        level=logging.INFO,
    )

    execution_start_time = datetime.datetime.now()
    print(f"Execution start time : {execution_start_time}")
    logging.info(f"Script Execution start at : {execution_start_time}")
except Exception as _e:
    logging.error(f"Error in creating log file : {repr(_e)}")
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
chrome_options.binary_location = "/usr/bin/google-chrome"
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument('--headless=new')
# chrome_options.headless = True

preferences = {
    "profile.default_content_settings.popups": 0,
    "download.default_directory": "/home/shubh/Desktop/AGL/chrome-headless/plaReports",
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

reports_url = "https://advertising.flipkart.com/ad-account/reports/others?baccount=RSAUFLMCSZ&aaccount=C18XVZJB4GD7"


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


def selectAndClickAdProductDropDown() -> None:
    try:
        ad_product_dd = browser.find_element(
            By.CSS_SELECTOR,
            "#app > div:nth-child(1) > div:nth-child(1) > div > div.content > div > div.styles__StyledPlayArea-ihipf8-1.eGKFPt > div.styles__Container-sc-1b5k4zr-1.bSupBp > div:nth-child(1) > div:nth-child(1) > div.styles__DropdownContainer-sc-1k46dl-2.jOEHSJ > div > div",
        )
        time.sleep(2)
        ad_product_dd.click()
        time.sleep(2)
        logger.info(f"ad product dropdown clicked")
    except Exception as _e:
        logger.error(f"ad product dropdown not clicked{repr(_e)}")


def selectOptionFromAdProductDropDown(xpath: str = "") -> None:
    try:
        select_pca = browser.find_element(By.XPATH, xpath)  # fun call
        time.sleep(2)
        select_pca.click()
        time.sleep(2)
        logger.info(f"PLA option selected")
    except Exception as _e:
        logger.error(f"Error selecting PLA option {repr(_e)}")


def clickReportForOption():
    try:
        click_report = browser.find_element(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[1]/div/div[3]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div',
        )
        click_report.click()
        logger.info(f"click report for box clicked")
    except Exception as _e:
        logger.error(f"Error clicking report type box for pla {repr(_e)}")


def selectPlaReportOption():
    try:
        select_option = browser.find_element(
            By.XPATH, '//*[@id="popover-content"]/div/div[2]'
        )
        select_option.click()
        logger.info(f"flipkart supermart option selected")
    except Exception as _e:
        logger.error(f"error selecting option {repr(_e)}")


def selectAndClickReportDropdown() -> None:
    try:
        report_type_dd = browser.find_element(
            By.CSS_SELECTOR,
            "div.styles__Wrapper-sc-13lgkj1-0:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)",
        )
        time.sleep(2)
        report_type_dd.click()
        logger.info(f"report type drop down cliked")
        time.sleep(2)
    except Exception as _e:
        logger.error(f"Error click report type drop down {repr(_e)}")


def selectReportType(xpath: str = "") -> None:
    try:
        select_report_type = browser.find_element(By.XPATH, xpath)  # fn parmas
        time.sleep(2)
        select_report_type.click()
        time.sleep(2)
        logger.info(f"Report type selected")
    except Exception as _e:
        logger.error(f"Error selecting report type {repr(_e)}")


def selectAndClickDateBox() -> None:
    try:
        date_div = browser.find_element(By.CSS_SELECTOR, ".date")
        time.sleep(2)
        date_div.click()
        time.sleep(2)
        logger.info(f"date div box clicked")
    except Exception as _e:
        logger.error(f" Date div not found {repr(_e)}")


def selectDateRange() -> None:
    try:
        # clicking yesterday option to download n-1 day report where n is current date
        range_div = browser.find_element(
            By.XPATH, "/html/body/div/div[2]/div[6]/div/div/div/div[1]/div[2]"
        )
        time.sleep(2)
        range_div.click()
        time.sleep(2)
        logger.info(f"Range selected..")
    except Exception as _e:
        logger.error(f"Range not clicked or element not found {repr(_e)}")


def downloadReport() -> None:
    try:
        # clicking download btn to download the report
        download_btn = browser.find_element(
            By.CSS_SELECTOR, "button.styles__DefaultButton-sc-5941cr-1:nth-child(1)"
        )
        time.sleep(3)
        download_btn.click()
        logger.info(f"Download button clicked")
        time.sleep(5)
    except Exception as _e:
        logger.error(f"Error downloading selected report.")
    else:
        logger.info(f"Report download completed...")


def renameDownloadFile():

    rootdir = "/home/shubh/Desktop/AGL/chrome-headless/plaReports/"
    regex = re.compile("(.*csv$)")

    for root, dirs, files in os.walk(rootdir):
        for file in files:
            if regex.match(file):
                logger.info(f"Downloaded file name : {file}")
                old_name = f"/home/shubh/Desktop/AGL/chrome-headless/plaReports/{file}"
                new_name = (
                    f"/home/shubh/Desktop/AGL/chrome-headless/plaReports/downloaded.csv"
                )
                logger.info(f"changed file name : {new_name}")
                os.rename(old_name, new_name)
                logger.info(f"file name changed..")


def changeCSVColumn(report_type: str = "", campaign_type: str = "") -> None:

    df = pd.read_csv(
        r"/home/shubh/Desktop/AGL/chrome-headless/plaReports/downloaded.csv",
        skiprows=2,
    )
    df1 = pd.DataFrame(df)
    df1["report_type"] = report_type  # name change
    df1["created_on"] = datetime.datetime.today() - datetime.timedelta(days=1)
    df1["account"] = "Brand 1"
    df1["platform"] = "SM"

    if campaign_type == "pla" and report_type == "placement_report":
        df2 = df1.rename(
            columns={
                "Campaign ID": "campaign_id",
                "Campaign Name": "campaign_name",
                "Ad Group ID": "ad_group_id",
                "AdGroup Name": "ad_group_name",
                "Add to Baskets": "add_to_baskets",
                "Add to Basket Rate": "add_to_basket_rate",
                "Ad Spend": "ad_spend",
                "Average CPB (Cost Per Basket Addition)": "average_cpb_cost_per_basket_addition",
                "Units Sold (Direct)": "units_sold_direct",
                "Units Sold (Indirect)": "units_sold_indirect",
                "CVR": "cvr",
                "Direct Revenue": "direct_revenue",
                "Indirect Revenue": "indirect_revenue",
                "ROI (Direct)": "roi_direct",
                "ROI (Indirect)": "roi_indirect",
            }
        )
    elif campaign_type == "pla" and report_type == "search_report":
        df2 = df1.rename(
            columns={
                "Campaign ID": "campaign_id",
                "Campaign Name": "campaign_name",
                "Ad Group ID": "ad_group_id",
                "AdGroup Name": "ad_group_name",
                "Query": "query",
                "Ad Spend": "ad_spend",
                "Add to Baskets": "add_to_baskets",
                "Add to Basket Rate": "add_to_basket_rate",
                "Average Cost per Basket": "Average Cost per Basket",
                "Units Sold (Direct)": "units_sold_direct",
                "Units Sold (Indirect)": "units_sold_indirect",
                "Direct Revenue": "direct_revenue",
                "Indirect Revenue": "indirect_revenue",
                "Direct Conversion Rate in %": "direct_conversion_rate",
                "Indirect Conversion Rate in %": "indirect_conversion_rate",
                "ROI (Direct)": "roi_direct",
                "ROI (Indirect)": "roi_indirect",
            }
        )
    elif campaign_type == "pla" and report_type == "consolidated_fsn_report":
        df2 = df1.rename(
            columns={
                "Campaign ID": "campaign_id",
                "Campaign Name": "campaign_name",
                "Ad Group ID": "ad_group_id",
                "AdGroup Name": "adgroup_name",
                "FSN ID": "fsn_id",
                "Product Name": "product_name",
                "Ad Spend": "ad_spend",
                "Add to Baskets": "add_to_baskets",
                "Add to Basket Rate": "add_to_basket_rate",
                "Average Cost per Basket": "Average Cost per Basket",
                "Units Sold (Direct)": "units_sold_direct",
                "Units Sold (Indirect)": "units_sold_indirect",
                "Direct Revenue": "direct_revenue",
                "Indirect Revenue": "indirect_revenue",
                "ROI (Direct)": "roi_direct",
                "ROI (Indirect)": "roi_indirect",
            }
        )
    elif campaign_type == "pla" and report_type == "keyword_report":
        df2 = df1.rename(
            columns={
                "Campaign ID": "campaign_id",
                "Campaign Name": "campaign_name",
                "AdGroup ID": "ad_group_id",
                "AdGroup Name": "adgroup_name",
                "Ad spend": "ad_spend",
                "Add to Baskets": "add_to_baskets",
                "Average CPC": "average_cpc",
                "Add to Basket Rate": "add_to_basket_rate",
                "Average Cost per Basket": "Average Cost per Basket",
                "Direct Units Sold": "direct_units_sold",
                "Indirect Units Sold": "indirect_units_sold",
                "Direct Conversion Rate in %": "direct_conversion_rate",
                "Direct Revenue": "direct_revenue",
                "Indirect Revenue": "indirect_revenue",
                "Click Through Rate in %": "click_through_rate",
                "Direct ROI": "direct_roi",
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


# logger.info(f"Process start for ConsolidatedDailyReport")
# def flipkartSupermartCampaignReportPlaConsolidatedDailyReport():
#     browser.get(reports_url)
#     time.sleep(5)
#     removePopUpBox()
#     time.sleep(2)
#     selectAndClickAdProductDropDown()
#     time.sleep(2)
#     selectOptionFromAdProductDropDown(xpath='//*[@id="popover-content"]/div/div[1]')
#     time.sleep(2)
#     clickReportForOption()
#     time.sleep(2)
#     selectPlaReportOption()
#     time.sleep(2)
#     selectAndClickReportDropdown()
#     time.sleep(2)
#     selectReportType(xpath='//*[@id="popover-content"]/div/div[2]')
#     logger.info(f"Consolidated Report type selected")
#     time.sleep(2)
#     selectAndClickDateBox()
#     time.sleep(2)
#     selectDateRange()
#     time.sleep(2)
#     downloadReport()
#     time.sleep(5)
#     renameDownloadFile()
#     time.sleep(10)
#     insertDataIntoDB(report_type="campaign_report",table_name="'flipkart_supermart_campaign_report_pla'")
#     time.sleep(10)
#     removeLastDownloadedFile(path="/home/shubh/Desktop/AGL/chrome-headless/plaReports/*")
#     print("done")

# flipkartSupermartCampaignReportPlaConsolidatedDailyReport()
# logger.info(f"Process done for ConsolidatedDailyReport")
# time.sleep(5)


# flipkart_supermart_placement_report_pla -- Placement Performance Report
logger.info(f"Process start for PlacementPerformanceReport")


def flipkartSupermartPlacementReportPlaPlacementPerformanceReport():
    time.sleep(3)
    browser.get(reports_url)
    time.sleep(3)
    removePopUpBox()
    time.sleep(2)
    selectAndClickAdProductDropDown()
    time.sleep(2)
    selectOptionFromAdProductDropDown(xpath='//*[@id="popover-content"]/div/div[1]')
    time.sleep(2)
    clickReportForOption()
    time.sleep(2)
    selectPlaReportOption()
    time.sleep(2)
    selectAndClickReportDropdown()
    time.sleep(2)
    selectReportType(xpath='//*[@id="popover-content"]/div/div[6]')
    logger.info(f"Placement Report type selected")
    time.sleep(2)
    selectAndClickDateBox()
    time.sleep(2)
    selectDateRange()
    time.sleep(2)
    downloadReport()
    time.sleep(5)
    renameDownloadFile()
    time.sleep(10)
    insertDataIntoDB(
        df2=changeCSVColumn(report_type="placement_report", campaign_type="pla"),
        table_name="flipkart_supermart_placement_report_pla",
    )
    time.sleep(15)
    removeLastDownloadedFile(
        path="/home/shubh/Desktop/AGL/chrome-headless/plaReports/*"
    )
    print("done")


# flipkartSupermartPlacementReportPlaPlacementPerformanceReport()
# logger.info(f"Process done for PlacementPerformanceReport")
# time.sleep(5)


# flipkart_supermart_search_report_pla  -- Search Team Report
logger.info(f"Process start for SearchTeamReport")


def flipkartSupermartSearchReportPla():
    time.sleep(3)
    browser.get(reports_url)
    time.sleep(5)
    removePopUpBox()
    time.sleep(2)
    selectAndClickAdProductDropDown()
    time.sleep(2)
    selectOptionFromAdProductDropDown(xpath='//*[@id="popover-content"]/div/div[1]')
    time.sleep(3)
    clickReportForOption()
    time.sleep(3)
    selectPlaReportOption()
    time.sleep(3)
    selectAndClickReportDropdown()
    time.sleep(2)
    selectReportType(xpath='//*[@id="popover-content"]/div/div[5]')
    logger.info(f"Search Team Report type selected")
    time.sleep(2)
    selectAndClickDateBox()
    time.sleep(2)
    selectDateRange()
    time.sleep(2)
    downloadReport()
    time.sleep(5)
    renameDownloadFile()
    time.sleep(10)
    insertDataIntoDB(
        df2=changeCSVColumn(report_type="search_report", campaign_type="pla"),
        table_name="flipkart_supermart_search_report_pla",
    )
    time.sleep(30)
    removeLastDownloadedFile(
        path="/home/shubh/Desktop/AGL/chrome-headless/plaReports/*"
    )
    print("done")


# flipkartSupermartSearchReportPla()
# logger.info(f"Process done for SearchTeamReport for PLA")
# time.sleep(5)


# flipkart_supermart_consolidated_fsn_report_pla  --  Consolidated FSN Report  -- Not Data Found
logger.info(f"Process start for Consolidated FSN  Report")


def flipkartSupermartConsolidatedFsnReportPla():
    time.sleep(3)
    browser.get(reports_url)
    time.sleep(5)
    removePopUpBox()
    time.sleep(2)
    selectAndClickAdProductDropDown()
    time.sleep(2)
    selectOptionFromAdProductDropDown(xpath='//*[@id="popover-content"]/div/div[1]')
    time.sleep(2)
    clickReportForOption()
    time.sleep(2)
    selectPlaReportOption()
    time.sleep(2)
    selectAndClickReportDropdown()
    time.sleep(2)
    selectReportType(xpath='//*[@id="popover-content"]/div/div[1]')
    logger.info(f"Consolidated FSN  Report type selected")
    time.sleep(2)
    selectAndClickDateBox()
    time.sleep(2)
    selectDateRange()
    time.sleep(2)
    downloadReport()
    time.sleep(5)
    renameDownloadFile()
    time.sleep(10)
    insertDataIntoDB(
        df2=changeCSVColumn(report_type="consolidated_fsn_report", campaign_type="pla"),
        table_name="flipkart_supermart_consolidated_fsn_report_pla",
    )
    time.sleep(30)
    removeLastDownloadedFile(
        path="/home/shubh/Desktop/AGL/chrome-headless/plaReports/*"
    )
    print("done")


# flipkartSupermartConsolidatedFsnReportPla()
# logger.info(f"Process done for Consolidated FSN  Report for PLA")
# time.sleep(5)


# flipkart_supermart_keyword_report_pla -- Keyword Report
logger.info(f"Process start for Keyword Report")


def flipkartSupermartKeywordReportPla():
    time.sleep(3)
    browser.get(reports_url)
    time.sleep(5)
    removePopUpBox()
    time.sleep(2)
    selectAndClickAdProductDropDown()
    time.sleep(2)
    selectOptionFromAdProductDropDown(xpath='//*[@id="popover-content"]/div/div[1]')
    time.sleep(2)
    clickReportForOption()
    time.sleep(2)
    selectPlaReportOption()
    time.sleep(2)
    selectAndClickReportDropdown()
    time.sleep(2)
    selectReportType(xpath='//*[@id="popover-content"]/div/div[7]')
    logger.info(f"Keyword Report  type selected")
    time.sleep(2)
    selectAndClickDateBox()
    time.sleep(2)
    selectDateRange()
    time.sleep(2)
    downloadReport()
    time.sleep(5)
    renameDownloadFile()
    time.sleep(10)
    insertDataIntoDB(
        changeCSVColumn(report_type="keyword_report", campaign_type="pla"),
        table_name="flipkart_supermart_keyword_report_pla",
    )
    time.sleep(30)
    removeLastDownloadedFile(
        path="/home/shubh/Desktop/AGL/chrome-headless/plaReports/*"
    )
    print("done")


flipkartSupermartKeywordReportPla()
logger.info(f"Process done for Keyword Report for PLA")
time.sleep(5)

time.sleep(3)
browser.quit()
