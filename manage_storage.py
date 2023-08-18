import json

def load_json(file_name):
    # Read the JSON file
    with open('json/'+file_name +'.json') as file:
        data = json.load(file)
    return data

def get_tematic():
    data = load_json("config")
    tematic = data["tematic"]
    return tematic
