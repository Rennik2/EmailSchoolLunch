from botasaurus.browser import browser, Driver
from botasaurus.soupify import soupify
from bs4 import BeautifulSoup

import SendEmail

@browser
def scrape_lunch_table_task(driver: Driver, data):
    driver.google_get("https://www.sandomenicocafe.com/")

    html = (BeautifulSoup(driver.page_html, "html.parser")).prettify()

    TableStart = html.find('id="elementor-tab-content-127') 
    TableStart = TableStart + html[TableStart:].find('>') + 1       # don't include the <dic> line of html code
    TableEnd = html[TableStart:].find('</div>') + TableStart

    Table = html[TableStart:TableEnd]
    
    SendEmail.send_email("sandomenicolunch+test@gmail.com", html, "test", "html")
    # Save the data as a JSON file in output/scrape_lunch_table_task.json
    return Table

scrape_lunch_table_task()