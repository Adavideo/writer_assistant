from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from instructions_templates import context_template, tasks_template, information_template
from manage_storage import get_tematic, get_episode_summary


def get_instructions_template():
    instructions_template = context_template + information_template + tasks_template
    return instructions_template

def generate_messages(episode_number, user_input):
    #Prepare templates
    instructions_template = get_instructions_template()
    system_message_prompt = SystemMessagePromptTemplate.from_template(instructions_template)
    human_template = "{user_input}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    #Generate messages
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    messages = chat_prompt.format_messages( tematic=get_tematic(),
                                            episode_number=episode_number,
                                            episode_summary = get_episode_summary(episode_number),
                                            user_input=user_input)
    return messages
