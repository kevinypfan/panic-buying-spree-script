import json
def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError:
        return False
    return True