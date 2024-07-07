import datetime
import ScrapeLunchMenu
import SendEmail 


today = datetime.date.today().strftime("%A")
LunchToDay_html = ScrapeLunchMenu.scrape_lunch_table_task()

Subject = today + "'s Menu"

SendEmail.send_email("sandomenicolunch+test@gmail.com", LunchToDay_html, Subject, "html")


