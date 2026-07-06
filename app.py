import streamlit as st
import google.generativeai as genai
import os

st.title("🌐 NHS AIs - Vera Intelligence")

# API Key check
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Model selection (ye version zyada stable hai)
model = genai.GenerativeModel('gemini-pro')

user_input = st.text_input("Ask anything:")

if st.button("Analyze"):
    if user_input:
        try:
            response = model.generate_content(user_input)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")
