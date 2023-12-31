import load_keys
from langchain.chat_models import ChatOpenAI
from messages import generate_messages
from episodes_navigator import select_episode

chat_model = ChatOpenAI()
episode_number = select_episode()
user_input = "."
while user_input !="":
    user_input=input("How can I help you?: ")
    messages = generate_messages(episode_number, user_input)
    output = chat_model.predict_messages(messages)
    print(output.content)
