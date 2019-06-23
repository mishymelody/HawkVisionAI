# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC4eac21d5a3a04c59ccbb64b03c6aac03'
auth_token = 'd28cdb8229cbb9e93c1bc711c7f8be4e'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Yo police! theres an offender here. come here fast at the speed of light",
                     from_='+12268941582',
                     to='+16476403703'
                 )
