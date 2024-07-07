
import ScrapeLunchMenue
import SendEmail 


html = """
<html>
  <body>

  <h1>This is a Heading</h1>
  <p>This is a paragraph pt2.</p>

  </body>
</html>
"""


LunchToDay = ScrapeLunchMenue.scrape_lunch_table_task()

SendEmail.send_email("sandomenicolunch+test@gmail.com", LunchToDay, "other", "html")


