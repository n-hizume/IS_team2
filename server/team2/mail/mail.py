import json
from .models import Mail
from . import gmailApi
from django.db import IntegrityError

# 結局使わない
class OriginalMail:
    def __init__(self, title, to, fr, body, date) -> None:
        self.title = title
        self.to = to
        self.fr = fr
        self.body = body
        self.date = date

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
    
    def original2json(self):
        mail_dict = {}
        mail_dict["mail"] = {}
        mail_dict["mail"]["id"] = self.id
        mail_dict["mail"]["title"] = self.title
        mail_dict["mail"]["to"] = self.to
        mail_dict["mail"]["from"] = self.fr
        mail_dict["mail"]["body"] = self.body
        json_data = json.dumps(mail_dict, ensure_ascii=False)
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
    send_dict = json.loads(json_data)
    access_token = send_dict["auth"]["token"]
    refresh_token = send_dict["auth"]["refresh_token"]
    expiry_date = send_dict["auth"]["expiry"]
    to = send_dict["mail"]["to"]
    subject = send_dict["mail"]["subject"]
    body = send_dict["mail"]["body"]
    manager = gmailApi.GmailApiManager()
    try:
        res = manager.send_mail(access_token, refresh_token, expiry_date, to, subject, body)
    except:
        res = {}
    return res

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
    json_data = json.dumps(mails_dict, ensure_ascii=False)
    return json_data

def get_token(json_auth):
    auth_dict = json.loads(json_auth)
    code = auth_dict["code"]
    redirect_url = auth_dict["redirect_url"]
    manager = gmailApi.GmailApiManager()
    res = manager.get_token(code, redirect_url)

    return json.dumps(res, ensure_ascii=False)
    
    