from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from apiclient import errors
from email.mime.text import MIMEText
from creds.app import APP_CONFIG
import base64
import json
import requests
from urllib.parse import quote
from dateutil import parser
import pytz

class GmailApiManager:
    def __init__(self):
        info = APP_CONFIG
        self.CLIENT_ID = info["web"]["client_id"]
        self.CLIENT_SECRET = info["web"]["client_secret"]

        self.SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

    def get_service(self, access_token, refresh_token, expiry_date):
        user_info = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "access_token": access_token,
            "refresh_token": refresh_token,
            expiry_date: expiry_date
        }

        creds = Credentials.from_authorized_user_info(user_info, self.SCOPES)

        if not creds.valid:
            creds.refresh(Request())

        service = build('gmail', 'v1', credentials=creds)

        return service

    def parse_date(self, date_str):
        date = parser.parse(date_str)
        date = date.astimezone(pytz.timezone('Asia/Tokyo'))
        return date.strftime("%Y/%m/%dT%H:%M:%S+09:00")
    
    def parse_mail_detail(self, detail):
        body = []
        if 'data' in detail['payload']['body']:
            body.append(base64.urlsafe_b64decode(detail["payload"]["body"]["data"]).decode("UTF-8"))
        else:
            for part in detail["payload"]["parts"]:
                if 'data' in part["body"]:
                    body.append( base64.urlsafe_b64decode(part["body"]["data"]).decode("UTF-8") )

        return {
            "id": detail["id"],
            "threadId": detail["threadId"],
            "snipet": detail["snippet"],
            "body": body,
            "subject": [ header["value"] for header in detail["payload"]["headers"] if header["name"].lower() == "subject"][0],
            "from": [ header["value"] for header in detail["payload"]["headers"] if header["name"].lower() == "from"][0],
            "to": [ header["value"] for header in detail["payload"]["headers"] if header["name"].lower() == "to"][0],
            "date": [ self.parse_date(header["value"]) for header in detail["payload"]["headers"] if header["name"].lower() == "date"][0],
        }
    
    
    def get_message_list(self, access_token, refresh_token, expiry_date):
        service = self.get_service(access_token, refresh_token, expiry_date)
        messages = []

        max_results = 100
        # query = "label:CATEGORY_PERSONAL label:demo"
        query=""

        try:
            message_ids = (
                service.users()
                .messages()
                .list(userId="me", maxResults=max_results, q=query)
                .execute()
            )

            if message_ids["resultSizeEstimate"] == 0:
                return []
            
            for message_id in message_ids["messages"]:
                # 各メッセージ詳細
                detail = (
                    service.users()
                    .messages()
                    .get(userId="me", id=message_id["id"])
                    .execute()
                )
                
                message = self.parse_mail_detail(detail)
                # print(detail)
                messages.append(message)

        except errors.HttpError as error:
            print("An error occurred: %s" % error)


        return messages
    
    def create_message(self, to, subject, body):
        message = MIMEText(body)
        message["to"] = to
        message["from"] = "me"
        message["subject"] = subject

        encode_message = base64.urlsafe_b64encode(message.as_bytes())
        return {"raw": encode_message.decode()}
    
    def send_mail(self, access_token, refresh_token, expiry_date, to, subject, body):
        service = self.get_service(access_token, refresh_token, expiry_date)

        message = self.create_message(to, subject, body)
        res = (
            service.users()
            .messages()
            .send(userId="me", body=message)
            .execute()
        )

        return res
    
    def delete_label(self, access_token, refresh_token, expiry_date, mail_id):
        service = self.get_service(access_token, refresh_token, expiry_date)
        res = (
            service.users()
            .labels(userId="me", id=mail_id)
        )

    def get_token(self, code, redirect_url):
        url = "https://oauth2.googleapis.com/token"
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'charset': "UTF-8"
        }
        content = 'code=' + code
        content += '&client_id=' + self.CLIENT_ID
        content += '&client_secret=' + self.CLIENT_SECRET
        content += '&redirect_uri=' + quote(redirect_url)
        content += '&grant_type=authorization_code&access_type=offline'

        r = requests.post(url, data=content, headers=headers)
        print(r.text)
        return json.loads(r.text)



def get_sample_user_info():
    with open("creds/sample_user_credentials.json") as f:
        info = json.load(f)

    return {
        "access_token": info["access_token"],
        "refresh_token": info["refresh_token"],
        "expiry_date": info["expiry_date"]
    }


if __name__ == '__main__':
    user_info = get_sample_user_info()
    manager = GmailApiManager()
    messages = manager.get_message_list(user_info["access_token"], user_info["refresh_token"], user_info["expiry_date"])
    if messages:
        for message in messages:
            print(message)
    
    # res = manager.send_mail(user_info["access_token"], user_info["refresh_token"], user_info["expiry_date"], "hizumee228@gmail.com", "APIテスト", "こんにちは。\nこれはテストです。")
    # print(res)