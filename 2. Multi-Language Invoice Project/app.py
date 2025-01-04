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

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


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

input_prompt = '''
You are expert in understanding Invoices. We will upload image as invoice and you
will have to answer any questions based on the uploaded image
'''

## If ask button is clicked

if submit:
    image_data = input_image_setup(upload_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)