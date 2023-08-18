import load_keys
from langchain.chat_models import ChatOpenAI
from messages import generate_messages
from episodes_navigator import select_episode

chat_model = ChatOpenAI()
episode_number = select_episode()
user_input = "."
while user_input !="":
    user_input=input("user: ")
    messages = generate_messages(episode_number, user_input)
    print(messages[0])
    output = chat_model.predict_messages(messages)
    print(output.content)
