import sys
import ast
import streamlit as st # type: ignore
import base64
from main import RAGquery, add_file
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

def save_uploaded_file(uploaded_file, save_path):
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return save_path

with st.sidebar:
    uploaded_file = st.file_uploader("Add text file !")
    content = ""
    if uploaded_file:
        save_path = os.path.join(os.getcwd(), uploaded_file.name)
        save_path = save_uploaded_file(uploaded_file, save_path)
        st.success(f"saved to {save_path}")
        add_file(save_path)

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
