from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(
    api_key=os.getenv("GOOGLE_API+KEY"))



## funtoion to load Gemini Pro

model= genai.GenerativeModel("gemini-pro")
def getLLMResponse(question_str):
    response=model.generate_content(question_str)
    return response.text


st.set_page_config(
    page_title="Q&A"
)

st.header("Application")
input = st.text_input("Input :" , key ="input")

submit= st.button("Ask the Question")

if submit:
    response= getLLMResponse(input)
    st.subheader("The Response is")
    st.write(response)

    
