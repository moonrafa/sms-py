from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)
from_num = os.getenv('FROM_NUMBER')
to_num = os.getenv('TO_NUMBER')
message = client.messages.create(body='You have new updates on your account.', from_=[from_num]
, to=[to_num])
print(message.sid)
