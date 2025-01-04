from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from PIL import Image
import os
import google.generativeai as genai


api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-2.0-flash-exp')

def get_gemini_response(input,image,prompt):
    response =model.generate_content([input,image[0],prompt])
    return response.text

# Initialize our streamlit app
st.set_page_config(page_title='MultiLanguage Invoice Extractor')

st.header("MultiLanguage Invoice Extractor")

input = st.text_input("Input Prompt: ", key='input')
upload_file = st.file_uploader("Choose an Image of the Invoice...", type=['jpg', 'jpeg', 'png'])

image = ''

if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    
submit = st.button("Tell me about the Image")