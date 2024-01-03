from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(
    api_key=os.getenv("GOOGLE_API+KEY"))


model= genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def getLLMResponse(question_str):
    response=chat.send_message(question_str,stream=True)
    return response

st.set_page_config(
    page_title="Q&A App"
)
st.header("LLM Application from Q&A")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input= st.text_input("Input :",key="input")
submit= st.button("Start The Chat")

if submit and input:
    response= getLLMResponse(input)
    ## Add user Query in Session chat

    st.session_state['chat_history'].append(("You",input))
    st.subheader("The Response is ")

    for chun in response:
        st.write(chun.text)
        
    st.session_state['chat_history'].append((
        "Bot",chun.text)
    )
st.subheader("The Chat history")

for role , text in st.session_state['chat_history']:
    st.write(f"{role},{text}")
