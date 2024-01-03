from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(
    api_key=os.getenv("GOOGLE_API+KEY"))



## funtoion to load Gemini Pro

model= genai.GenerativeModel("gemini-pro-vision")
def getLLMResponse(question_str,input_img):
    if question_str!="":
        response=model.generate_content([question_str,input_img])
    else:
        response=model.generate_content(input_img)
    return response.text


st.set_page_config(
    page_title="IMage Demo"
)

st.header("Gemini Application")
input = st.text_input("Input Prompt :" , key ="input")

Uploade_file = st.file_uploader(
    "Choose an Image..",type=["jpg","jpeg","png"]
)
image=""
if Uploade_file is not None:
    image= Image.open(Uploade_file)
    st.image(image,caption="Uploaded Images.",use_column_width=True)

submit= st.button("Berif the Image")


if submit:
    response= getLLMResponse(input,image)
    st.subheader("The Response is")
    st.write(response)

    
