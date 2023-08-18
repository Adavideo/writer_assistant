from manage_storage import get_episode_tittle, get_episode_summary

def show_episode_information(episode_number):
    episode_tittle = get_episode_tittle(episode_number)
    episode_summary = get_episode_summary(episode_number)
    print("Episode "+str(episode_number) + ": " + episode_tittle)
    print("Summary: " + episode_summary)

def select_episode():
    episode_number = ""
    user_input = input("On what episode are we going to work?: ")
    while not episode_number:
        if user_input.isnumeric():
            episode_number = int(user_input)
        else:
            user_input = input("On what episode are we going to work? Please write a number: ")
    show_episode_information(episode_number)
    return episode_number
