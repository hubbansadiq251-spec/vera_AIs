import streamlit as st
import google.generativeai as genai
import os

st.title("🌐 NHS AIs - Vera Intelligence")

# Environment variable se key uthayein (jo humne Secrets mein daali hai)
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Basic model jo har jagah chalta hai
model = genai.GenerativeModel('gemini-pro')

user_input = st.text_input("Ask anything:")

if st.button("Analyze"):
    if user_input:
        try:
            response = model.generate_content(user_input)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
