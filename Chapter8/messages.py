#import message_activity
#from message_activity import *
#import message_activity as ma
#from message_activity import send_messages as sm
from message_activity import send_messages

messages = ["Hello, how are you?", "I hope you are doing well.", "I will see you again soon."]
sent_messages = []

def show_messages():
    for message in messages:
        print(message)

send_messages(messages, sent_messages)

print("messages list: ")
print(messages)

print("sent_messages list: ")
print(sent_messages)