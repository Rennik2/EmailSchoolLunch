
from SendEmail import Email


html = """
<html>
  <body>

  <h1>This is a Heading</h1>
  <p>This is a paragraph.</p>

  </body>
</html>
"""
e = Email()

e.sendEmail("sandomenicolunch+test@gmail.com", html, "other", "html")

