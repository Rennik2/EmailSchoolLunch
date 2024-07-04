from botasaurus.browser import browser, Driver
from botasaurus.soupify import soupify
from bs4 import BeautifulSoup

from botasaurus.browser import browser, Driver

@browser
def scrape_lunch_table_task(driver: Driver, data):
    driver.google_get("https://www.sandomenicocafe.com/")

    html = (BeautifulSoup(driver.page_html, "html.parser")).prettify()



    print(html)

    # Save the data as a JSON file in output/scrape_lunch_table_task.json
    return {
        "html": html
    }     

# Initiate the web scraping task
scrape_lunch_table_task()