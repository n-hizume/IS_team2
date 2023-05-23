import openai
import json
import re

from .creds.cred import API_KEY


class chatGptManager:
    def __init__(self):
        # with open("creds/gpt_credentials.json") as f:
        #     info = json.load(f)

        # openai.api_key = info["api_key"]
        openai.api_key = API_KEY

    def create_query(self, content, level=0):
        if level == 0:
            return f'「{content}」をローレベルな敬語に変換した文の例をいくつか挙げてください。'
        elif level == 1:
            return f'「{content}」をミドルレベルな敬語に変換した文の例をいくつか挙げてください。'
        else:
            return f'「{content}」をハイレベルな敬語に変換した文の例をいくつか挙げてください。'

    
    def parse_result(self, result: str):
        if '->' in result:
            result = result.split('->')[1]

        replace_list = ["・", "「", "」", "'", '"', " "]
        for replace in replace_list:
            result = result.replace(replace, "")
        return result

    def translate(self, content):
        structure = "・「ans1」\n・「ans2」\n..."

        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": self.create_query(content, level=0) 
                                + "\n回答は以下の形式に従ってください\n" 
                                + structure,
                },
            ],
        )

        body = res["choices"][0]["message"]["content"]
        results = body.split('\n')
        if len(results) < 1:
            return []
        
        return [self.parse_result(result) for result in results if result[0] == '・']
    

if __name__ == '__main__':
    manager = chatGptManager()
    print(manager.translate("お世話になります"))