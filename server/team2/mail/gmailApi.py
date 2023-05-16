from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from apiclient import errors
import base64
import json

class GmailApiManager:
    def __init__(self):
        with open("creds/app_credentials.json") as f:
            info = json.load(f)
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
    
    def parse_mail_detail(self, detail):

        body = []
        if 'data' in detail['payload']['body']:
            body.append(base64.urlsafe_b64decode(detail["payload"]["body"]["data"]).decode("UTF-8"))
        else:
            for part in detail["payload"]["parts"]:
                 body.append( base64.urlsafe_b64decode(part["body"]["data"]).decode("UTF-8") )

        return {
            "id": detail["id"],
            "threadId": detail["threadId"],
            "snipet": detail["snippet"],
            "body": body,
            "subject": [ header["value"] for header in detail["payload"]["headers"] if header["name"] == "Subject"][0],
            "from": [ header["value"] for header in detail["payload"]["headers"] if header["name"] == "From"][0],
            "to": [ header["value"] for header in detail["payload"]["headers"] if header["name"] == "To"][0],
            "date": [ header["value"] for header in detail["payload"]["headers"] if header["name"] == "Date"][0],
        }
    
    
    def get_message_list(self, access_token, refresh_token, expiry_date):
        service = self.get_service(access_token, refresh_token, expiry_date)
        messages = []

        max_results = 100
        query = "label:CATEGORY_PERSONAL label:demo"

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
                print(detail)
                messages.append(message)

        except errors.HttpError as error:
            print("An error occurred: %s" % error)


        return messages
    


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
            print(message["subject"])
    