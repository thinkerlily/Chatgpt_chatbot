import gradio as gr
import openai
import config


openai.api_key = config.OPENAI_API_KEY


  
messages = [{"role": "system", "content": 'You are a therapist.'}]

def transcribe(input):
    global messages

    

    messages.append({"role": "user", "content": input})
    print(input)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    
    result = response["choices"][0]["message"]
    messages.append(result)
    
    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return chat_transcript



ui=gr.Interface(fn=transcribe, inputs = "text",outputs = "text").launch()
