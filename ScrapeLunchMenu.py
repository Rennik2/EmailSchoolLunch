from botasaurus.browser import browser, Driver
from botasaurus.soupify import soupify
from bs4 import BeautifulSoup
import datetime

@browser
def scrape_lunch_table_task(driver: Driver, data):
    driver.google_get("https://www.sandomenicocafe.com/")

    html = (BeautifulSoup(driver.page_html, "html.parser")).prettify()

    TableStart = html.find('id="elementor-tab-content-127' + str(day_number()) + '"') 
    TableStart = TableStart + html[TableStart:].find('>') + 1       # don't include the <dic> line of html code
    TableEnd = html[TableStart:].find('</div>') + TableStart

    Table = html[TableStart:TableEnd]

    # Save the data as a JSON file in output/scrape_lunch_table_task.json
    return Table


def day_number():
    today = datetime.date.today().strftime("%A")

    if today   == "Monday":     return 1
    elif today == "Tuesday":    return 2
    elif today == "Wednesday":  return 3
    elif today == "Thursday":   return 4 
    elif today == "Friday":     return 5
    elif today == "Saturday":   return 6
    elif today == "Sunday":     return 7
