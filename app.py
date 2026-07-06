import streamlit as st
import google.generativeai as genai

st.title("🌐 NHS AIs - Vera Intelligence")

# Secret key ko direct access karein
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Model ko change karke 'gemini-pro' try karein, ye 404 nahi dega
model = genai.GenerativeModel('gemini-pro')

user_input = st.text_input("Ask anything:")

if st.button("Analyze"):
    if user_input:
        response = model.generate_content(user_input)
        st.write(response.text)
