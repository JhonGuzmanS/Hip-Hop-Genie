import sys
import ast
import streamlit as st # type: ignore
import base64
from main import RAGquery

#from datasets import load_dataset
#from sentence_transformers import SentenceTransformer 
# from transformers import AutoTokenizer, AutoModelForCausalLM

st.set_page_config(
    page_title="Hip Hop Genie",
    page_icon="🧞",
    layout="centered",
    initial_sidebar_state='auto'
)


if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.chat_message("user").markdown(prompt)
    response = RAGquery(prompt)
    with st.chat_message("assistant"):  
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})