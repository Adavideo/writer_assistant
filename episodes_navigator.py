
def select_episode():
    episode_number = ""
    user_input = input("On what episode are we going to work?: ")
    while not episode_number:
        if user_input.isnumeric():
            episode_number = int(user_input)
        else:
            user_input = input("On what episode are we going to work? Please write a number: ")
    return episode_number
