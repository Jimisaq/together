# app.py

import streamlit as st
from together import query_together_ai

st.set_page_config(page_title="Together with Jim")

st.title("💬 Together With Jim")

prompt = st.text_area("Your prompt:")
# temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
# max_tokens = st.slider("Max Tokens", 10, 500, 100)

if st.button("Submit"):
    if prompt.strip():
        response = query_together_ai(prompt, 100, 0.9)
        st.subheader("Response:")
        st.write(response)
    else:
        st.warning("Please enter a prompt.")
