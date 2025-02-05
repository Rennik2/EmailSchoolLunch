# import the mailjet wrapper
from mailjet_rest import Client
import os

# Get your environment Mailjet keys
api_key = os.environ['MJ_APIKEY_PUBLIC']
api_secret = os.environ['MJ_APIKEY_PRIVATE']



def send_email(recipient: str, message_body: str, subject: str, format: str = "plain"):
	mailjet = Client(auth=(api_key, api_secret))

	mailjet = Client(auth=(api_key, api_secret))
	if format == "plain":
		data = {
			'FromEmail': 'sandomenicolunch@gmail.com',
			'FromName': 'God',
			'Subject': subject,
			'Text-part': message_body,
			'Recipients': [{'Email': 'sandomenicolunch@gmail.com'}]
		}
	elif format == 'html':
		data = {
			'FromEmail': 'sandomenicolunch@gmail.com',
			'FromName': 'God',
			'Subject': subject,
			'Html-part': message_body,
			'Recipients': [{'Email': 'recipient'}]
		}
	else :
		raise Exception("${format} this does not make sense")

	result = mailjet.send.create(data=data)
	print(result.status_code)
	print(result.json())