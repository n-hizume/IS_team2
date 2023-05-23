import json
import chatGptApi

def translate(json_data):
    pre_dict = json.loads(json_data)
    pre_str = pre_dict["word"]
    manager = chatGptApi.chatGptManager()
    keigo_str_list = manager.translate(pre_str)
    keigo_dict = {}
    keigo_dict["translated_words"] = keigo_str_list
    json_keigo = json.dumps(keigo_dict)
    return json_keigo