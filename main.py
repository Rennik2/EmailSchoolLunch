import datetime 
import schedule
import time 

import ScrapeLunchMenu
import SendEmail 

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


send_lunch_menu()

# schedule.every().day.at("11:14").do(send_lunch_menu)

# try: 
#     print("Terminate programe with Ctrl+C")

#     while True:
#         try:
#             schedule.run_pending()
#             time.sleep(10)
            
#         except Exception as e:
#             SendEmail.send_email("sandomenicolunch+error@gmail.com", str(e), "AN ERROR ACCURRED")
#             print(f"An error occurred: {e}")
# except KeyboardInterrupt:
#     SendEmail.send_email("sandomenicolunch+error@gmail.com", "Program terminated by user", "AN ERROR ACCURRED")
#     print("Program terminated by user")
