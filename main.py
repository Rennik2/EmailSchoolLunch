import datetime
import ScrapeLunchMenu
import SendEmail 
import schedule
import time 

def send_lunch_menu():
    today = datetime.date.today().strftime("%A") 
    LunchToDay_html_table = ScrapeLunchMenu.scrape_lunch_table_task() 

    Subject = today + "'s Menu"

    with open("TestEmailList.txt", 'r') as file:
        for email in file.readlines():
            if email.find('@') != -1 and email[email.find('@'):].find('.') != -1: # check if its an email. Could be better
                SendEmail.send_email(email, LunchToDay_html_table, Subject, "html")
            else:
                print(f"Email doesn't work: {email}")


schedule.every().day.at("07:30").do(send_lunch_menu)

while True:
    try:
        schedule.run_pending()
        time.sleep(10)
        

    except Exception as e:
        SendEmail.send_email("sandomenicolunch+error@gmail.com", str(e), "an error occurred", )
        print(f"An error occurred: {e}")

