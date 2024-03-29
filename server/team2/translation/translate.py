import json
from . import chatGptApi

def translate(json_data):
    pre_dict = json.loads(json_data)
    pre_str = pre_dict["word"]
    pre_level = pre_dict["level"]
    manager = chatGptApi.chatGptManager()
    keigo_str_list = manager.translate(pre_str, level=pre_level)
    keigo_dict = {}
    keigo_dict["translated_words"] = keigo_str_list
    json_keigo = json.dumps(keigo_dict, ensure_ascii=False)
    return json_keigo