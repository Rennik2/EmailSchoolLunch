import os.path
import base64

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from email.mime.text import MIMEText

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


def sendEmail(recipient: str, message_body: str, subject: str, format: str = "plain"):

  creds = makeCredentials()

  if format == "plain":
    message = MIMEText(message_body)
  if format == 'html':
    message = MIMEText(message_body, 'html')
  
  message['to'] = recipient
  message['subject'] =  subject
  create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

  try:
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)

    message = (service.users().messages().send(userId = "me", body = create_message).execute())
    print('Message sent succesfuly!')

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")


def makeCredentials():
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  return creds 


html = """
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
"""

sendEmail("sandomenicolunch+test@gmail.com", html, "other", 14)

