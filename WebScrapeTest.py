from botasaurus.browser import browser, Driver
from botasaurus.soupify import soupify
from bs4 import BeautifulSoup


@browser
def scrape_lunch_table_task(driver: Driver, data):
    driver.google_get("https://www.sandomenicocafe.com/")

    html = (BeautifulSoup(driver.page_html, "html.parser")).prettify()
    table_start = html.find('id="elementor-tab-content-1271"')
    table_end = html[table_start:].find('</div>') + table_start

    print(html[table_start:table_end])
    print(table_start, table_end)

    # Save the data as a JSON file in output/scrape_lunch_table_task.json
    return {
        "html": html[table_start:table_end]
    }     

# Initiate the web scraping task
scrape_lunch_table_task()