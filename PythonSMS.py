from twilio.rest import Client
import json

with open('creds.json') as f:
    secrets = json.load(f)

account_sid = secrets["account_sid"]
auth_token = secrets["auth_token"]
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12564155837',
    body='I cannot believe this works!',
    to='+19374227609'
)

print(message.sid)
