from dotenv import load_dotenv
load_dotenv()  # loading all .env files

import streamlit as st
import os
import google.generativeai as genai

# Securely fetch API key
api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


# Intializing streamlit app
st.set_page_config(page_title='QnA Demo')

st.header("Gemini LLM Application")

input = st.text_input("Input: ", key='input')

submit = st.button("Ask the Question")

# when submit is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("The response is ")
    st.write(response)