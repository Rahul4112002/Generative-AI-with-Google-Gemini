from dotenv import load_dotenv
from streamlit_extras.add_vertical_space import add_vertical_space
load_dotenv()

import streamlit as st 

import os

import sqlite3

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])    
    return response.text

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION and MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

## Streamlit App
# Set page configuration
st.set_page_config(
    page_title="Gemini App: Retrieve Any SQL Query",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar configuration
with st.sidebar:
    st.title("Gemini App")
    st.image("gemini.jpg", caption="Powered by Gemini AI", use_column_width=True)
    st.markdown("### Features:")
    st.markdown("""
    - Retrieve SQL queries easily
    - Simple and user-friendly interface
    - Database: `student.db`
    """)
    add_vertical_space(2)
    st.write("Made with ❤️ by Rahul John")

# Main page layout
st.title("💎 Gemini App")
st.subheader("Retrieve Any SQL Query with Ease")

st.markdown("""
Welcome to the **Gemini App**! Enter your question, and our AI will generate the corresponding SQL query and retrieve data from the database for you.
""")

# Input section
st.write("### Input your query below:")
question = st.text_input("Enter your question:", placeholder="E.g., Show all students with grades above 90")

# Submit button
if st.button("Ask the Question"):
    if question.strip():
        with st.spinner("Generating SQL query..."):
            try:
                # Simulate AI response and database query (replace with your actual functions)
                response_sql = get_gemini_response(question, prompt)
                st.code(response_sql, language="sql")
                response_data = read_sql_query(response_sql, "student.db")

                # Display results
                st.success("Query executed successfully!")
                st.subheader("Query Results:")
                if response_data:
                    st.write(response_data)
                else:
                    st.warning("No data found.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid question.")

# Footer
st.markdown("---")
st.caption("© 2025 Gemini App. All rights reserved.")