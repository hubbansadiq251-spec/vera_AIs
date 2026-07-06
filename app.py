import streamlit as st
import google.generativeai as genai

st.title("🌐 NHS AIs - Vera Intelligence")

# API Key
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Model setup
model = genai.GenerativeModel('gemini-1.5-flash')

user_input = st.text_input("Ask anything:")

# Button click hone par aur input hone par hi code chale
if st.button("Analyze"):
    if user_input:
        try:
            response = model.generate_content(user_input)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question first!")
