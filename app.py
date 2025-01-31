import chainlit as cl
from src.llm import ask_order,messages


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...

    #append the user response
    messages.append({"role":"user","content": message.content})
    # give the message to the function
    response=ask_order(messages)


    # Append the assistant response
    messages.append({"role":"assistant","content": response})

    # Send a response back to the user(chainlit )
    await cl.Message(
        # send this response to my frontend
        content=response,
    ).send()
