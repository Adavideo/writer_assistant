import load_keys
from langchain.chat_models import ChatOpenAI
from messages import generate_messages


chat_model = ChatOpenAI()
user_input = "."
while user_input !="":
    user_input=input("user: ")
    messages = generate_messages(user_input)
    output = chat_model.predict_messages(messages)
    print(output.content)
