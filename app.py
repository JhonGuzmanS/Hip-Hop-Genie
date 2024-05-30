import sys
import ast
import streamlit as st # type: ignore
import base64
from main import RAGquery
import os
from dotenv import load_dotenv

#from sentence_transformers import SentenceTransformer 
#from transformers import AutoTokenizer, AutoModelForCausalLM

st.set_page_config(
    page_title="Hip Hop Genie",
    page_icon="🧞",
    layout="centered",
    initial_sidebar_state='auto'
)

with st.sidebar:
    uploaded_file = st.file_uploader("Add text file !")
    content = ""
    if uploaded_file:
        st.write("thank you!")

    st.header("Welcome")

load_dotenv()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)
    response = RAGquery(prompt)
    with st.chat_message("assistant"):  
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
