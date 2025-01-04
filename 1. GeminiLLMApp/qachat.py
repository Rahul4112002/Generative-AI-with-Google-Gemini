from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Securely fetch API key
api_key = os.getenv("GOOGLE_API_KEY")

# Configure the GenAI model
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_gemini_response(question):
    # Send a message and collect the streamed response
    response = chat.send_message(question, stream=True)
    final_text = ""
    for chunk in response:
        final_text += chunk.text
    return final_text

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input and button
user_input = st.text_input("Input: ", key='input')
submit = st.button("Submit")

if submit and user_input:
    # Fetch the model response
    response = get_gemini_response(user_input)
    
    # Add user input and bot response to chat history
    st.session_state['chat_history'].append(("You", user_input))
    st.session_state['chat_history'].append(("Bot", response))
    
    # Display the response
    st.subheader("The Response is")
    st.write(response)

# Display chat history
st.subheader("The Chat History")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
