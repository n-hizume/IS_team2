import openai

from .creds.cred import API_KEY


class chatGptManager:
    def __init__(self):
        openai.api_key = API_KEY

    def create_query(self, content, level=0):
        level_str = ""
        if level == 0:
            level_str = "少し丁寧"
        elif level == 1:
            level_str = "丁寧"
        else:
            level_str = "かなり丁寧"
        
        return f'「{content}」という言葉を、{level_str}な敬語に言い換えた例をいくつか挙げてください。'

    
    def parse_result(self, result: str):
        if '->' in result:
            result = result.split('->')[1]

        replace_list = ["・", "「", "」", "'", '"', " "]
        for replace in replace_list:
            result = result.replace(replace, "")
        return result

    def translate(self, content, level=0):
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": self.create_query(content, level=level) 
                                + '\n回答は以下の形式のように、先頭に"・"をつけて箇条書きにしてください。\n'
                                + "・「ans1」\n・「ans2」\n..."
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