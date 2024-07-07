import datetime
import ScrapeLunchMenu
import SendEmail 


today = datetime.date.today().strftime("%A")
LunchToDay_html = ScrapeLunchMenu.scrape_lunch_table_task()

Subject = today + "'s Menu"

with open("TestEmailList.txt", 'r') as file:
    for line in file.readlines():
        if line.find('@') != -1 and line[line.find('@'):].find('.') != -1:
            SendEmail.send_email(line, LunchToDay_html, Subject, "html")
        else:
            print(f"Email doesn't work: {line}")


