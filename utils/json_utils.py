__author__ = 'noah'

import json

def json_to_string(jsonObj):
    json_dump = json.dumps(jsonObj, ensure_ascii=False, indent=4)
    return json_dump.encode('utf-8')