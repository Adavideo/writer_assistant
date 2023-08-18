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

def get_episode_tittle(episode_number):
    episodes_list = load_json("episodes_list")
    episode_information = episodes_list["episodes"][episode_number-1]
    title = episode_information["title"]
    return title

def get_episode_summary(episode_number):
    episodes_list = load_json("episodes_list")
    episode_information = episodes_list["episodes"][episode_number-1]
    summary = episode_information["summary"]
    return summary
