import requests
import json


def notice_message(channel, attachments):
    attachments = json.dumps(attachments)
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+ Token},
        data={"channel": channel,"attachments": attachments})
        #data={"channel": channel, "text": text ,"attachments": attachments})
