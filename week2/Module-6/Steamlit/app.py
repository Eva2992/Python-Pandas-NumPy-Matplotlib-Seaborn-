from google import genai     #pip install google-genai
import streamlit as st       #pip install streamlit
import os
from dotenv import load_dotenv       #pip install python-dotenv

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="give me an idea of gemini api"
)

st.markdown(response.text)

# for running ->  python -m streamlit run app.py

