import re 

from urllib.request import urlopen


url = "https://www.dreamhorse.com/"

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)
# title_index = html.find("<title>")

# start_index = title_index + len("<title>")
# end_index = html.find("</title>")

# print(html[start_index:end_index])