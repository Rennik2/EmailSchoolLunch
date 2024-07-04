# import requests

# from urllib.request import urlopen


# url = "https://www.sandomenicocafe.com"

# page = urlopen(url)
# html_bytes = page.read()
# html = html_bytes.decode("utf-8")


# print(html)





from botasaurus.request import request, Request
from botasaurus.soupify import soupify
from bs4 import BeautifulSoup

@request
def scrape_heading_task(request: Request, data):
    # Visit the Omkar Cloud website
    response = request.get("https://www.sandomenicocafe.com/")

    # Create a BeautifulSoup object    
    soup = soupify(response)
    
    # Retrieve the heading element's text
    site = soup.decode("utf-8")
    doc = BeautifulSoup(site, "html.parser")
    print(doc.prettify())
    # Save the data as a JSON file in output/scrape_heading_task.json
    return {
        "heading": doc.prettify()
    }     
# Initiate the web scraping task
scrape_heading_task()