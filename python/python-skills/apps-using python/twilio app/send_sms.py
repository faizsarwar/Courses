from twilio.rest import Client
from credential import *

client= Client(account_sid,auth_token)

our_msg="hey my sg is this !!!!!!!"

message= client.messages.create(to=my_cell,from_=my_twilio,body=our_msg)