import streamlit as st
import google.generativeai as genai

st.title("🌐 NHS AIs - Vera Intelligence")

# API Key fetching from Streamlit Secrets
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# 404 Error ko khatam karne ke liye full path name use kar rahe hain
model = genai.GenerativeModelmodel('gemini-1.0-pro')

user_input = st.text_input("Ask anything:")

if st.button("Analyze"):
    if user_input:
        try:
            response = model.generate_content(user_input)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question first!")
