from dotenv import load_dotenv
load_dotenv()  # loading all .env files

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Securely fetch API key
api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input,image):
    if input!="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Intializing streamlit app
st.set_page_config(page_title='QnA Demo')

st.header("Gemini LLM Application")

input = st.text_input("Input: ", key='input')

upload_file = st.file_uploader("Choose an Image...", type=['jpg', 'jpeg', 'png'])

image = ''

if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    
submit = st.button("Tell me about the Image")

# when submit is clicked
if submit:
    response = get_gemini_response(input,image)
    st.subheader("The response is ")
    st.write(response)