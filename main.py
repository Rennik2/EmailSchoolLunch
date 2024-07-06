
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
SendEmail.sendEmail("sandomenicolunch+test@gmail.com", html, "other", "html")



ScrapeLunchMenue.scrape_lunch_table_task()

