import streamlit as st
import google.generativeai as genai

st.title("🌐 NHS AIs - Vera Intelligence")

# Yahan apni API key quotes ke andar seedhi likhein (Testing ke liye)
genai.configure(api_key="AQ.Ab8RN6Kya3dxmhP9BLUhP-s9HWLVTaJyk3zfsuL__sv0WmOyhA")

model = genai.GenerativeModel('gemini-pro')

user_input = st.text_input("Ask anything:")

if st.button("Analyze"):
    if user_input:
        try:
            response = model.generate_content(user_input)
            st.write(response.text)
        except Exception as e:
            st.write("Error details:", e)
