import streamlit as st
import google.generativeai as genai

st.title("🌐 NHS AIs - Vera Intelligence")

# Yahan apni API key quotes ke andar seedhi likhein (Testing ke liye)
genai.configure(api_key="PASTE_YOUR_ACTUAL_API_KEY_HERE_WITHOUT_QUOTES_AROUND_THE_WHOLE_COMMAND")

model = genai.GenerativeModel('gemini-pro')

user_input = st.text_input("Ask anything:")

if st.button("Analyze"):
    if user_input:
        try:
            response = model.generate_content(user_input)
            st.write(response.text)
        except Exception as e:
            st.write("Error details:", e)
