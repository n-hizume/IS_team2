import json
import chatGptApi

# TODO
# jsonの仕様が決まったら変更
def translate(json_data):
    dict = json.loads(json_data)
    pre_str = dict["str"]
    manager = chatGptApi.chatGptManager()
    keigo_str = manager.translate(pre_str)
    keigo_dict = {}
    keigo_dict["str"] = keigo_str
    json_keigo = json.dumps(keigo_dict)
    return json_keigo

