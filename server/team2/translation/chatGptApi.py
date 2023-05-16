import openai
import json


class chatGptManager:
    def __init__(self):
        with open("creds/gpt_credentials.json") as f:
            info = json.load(f)

        openai.api_key = info["api_key"]

    def create_query(self, content, level=0):
        return f'「{content}」をより丁寧な敬語に変換した文の例をいくつか挙げ、「、」で区切って回答してください'

    def translate(self, content):
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": self.create_query(content, level=0)
                },
            ],
        )

        return res["choices"][0]["message"]["content"].split("、")
    

if __name__ == '__main__':
    manager = chatGptManager()
    print(manager.translate("お世話になります"))