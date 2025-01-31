# updated version of Openai
from openai import OpenAI
from src.prompt import system_instruction

# create an client object 
client=OpenAI()


messages=[
    {"role":"system","content":system_instruction},
]

# create a function that will give what user will ask
def ask_order(message, model="gpt-3.5-turbo", temperature=0):
    response=client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,

    )


    return response.choices[0].message.content
