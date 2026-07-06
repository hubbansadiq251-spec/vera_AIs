import streamlit as st
import google.generativeai as genai
import os

st.title("🌐 NHS AIs - Vera Intelligence")
api_key = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

user_input = st.text_input("Ask anything:")
if st.button("Analyze"):
    response = model.generate_content(user_input)
    st.write(response.text)