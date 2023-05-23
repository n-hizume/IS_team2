import json
import datetime
from .models import Mail
import gmailApi
from django.db import IntegrityError

class OriginalMail:
    def __init__(self, title, to, fr, body, date) -> None:
        self.title = title
        self.to = to
        self.fr = fr
        self.body = body
        self.date = date

    # メール送信用
    @classmethod
    def json2original(cls, json_data):
        d = json.loads(json_data)
        mail_dict = d["mail"]
        title = mail_dict["title"]
        to = mail_dict["to"]
        fr = mail_dict["from"]
        body = mail_dict["body"]
        date = mail_dict["date"]
        original = cls(title, date, fr, to, body)
        return original
    
    # もう使わないかも
    def original2json(self):
        mail_dict = {}
        mail_dict["mail"] = {}
        mail_dict["mail"]["id"] = self.id
        mail_dict["mail"]["title"] = self.title
        mail_dict["mail"]["to"] = self.to
        mail_dict["mail"]["from"] = self.fr
        mail_dict["mail"]["body"] = self.body
        json_data = json.dumps(mail_dict)
        return json_data        


# データベース操作

def get(id):
    if Mail.objects.filter(ThreadId=id).exists():
        mail = Mail.objects.get(ThreadId=id)
    else:
        mail = None
    return mail   

def insert(id, expiry_time):
    try:
        Mail.objects.create(ThreadId=id, ExpiryTime=expiry_time)
    except IntegrityError as e:
        print(f"error: {e}")

# フィールドが増えたら値をリストか辞書で受け取る
def update(id, expiry_time):
    try:
        mail = Mail.objects.get(ThreadId=id)
        mail.ExpiryTime = expiry_time
        mail.save()
    except Mail.DoesNotExist as e:
        print(f"error: {e}")

def delete(id):
    try:
        mail = Mail.objects.get(ThreadId=id)
        mail.delete()
    except Mail.DoesNotExist as e:
        print(f"error: {e}")

# メール関連処理

# 受信メールに締め切り日時のデータを追加
def add_expiry(mail_dict):
    id = mail_dict["threadId"]
    mail = get(id)
    if mail:
        expiry = mail.ExpiryTime
        expiry_str = expiry.strftime("%Y/%m/%d %H:%M:%S")
    else:
        expiry_str = ""
    mail_dict["expiry"] = expiry_str  

# TODO
# メール送信
def send_mail(json_data):
    original = OriginalMail.json2original(json_data)
    body = original.body

# メール受信
def get_mails(json_auth):
    auth_dict = json.loads(json_auth)
    access_token = auth_dict["auth"]["token"]
    refresh_token = auth_dict["auth"]["refresh_token"]
    expiry_date = auth_dict["auth"]["expiry"]
    manager = gmailApi.GmailApiManager()
    messages = manager.get_message_list(access_token, refresh_token, expiry_date)
    for message in messages:
        add_expiry(message)
    mails_dict = {}
    mails_dict["mails"] = messages
    json_data = json.dumps(mails_dict)
    return json_data