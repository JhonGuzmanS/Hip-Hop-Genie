import sys
import ast
import streamlit as st
import base64
import os
from dotenv import load_dotenv

import pandas as pd
import pymongo

from datasets import load_dataset
from sentence_transformers import SentenceTransformer 
from transformers import AutoTokenizer, AutoModelForCausalLM

st.set_page_config(
    page_title="Hip Hop Genie",
    page_icon="🧞",
    layout="centered",
    initial_sidebar_state='auto'
)

dataset = load_dataset("huggingartists/drake")

# Convert the dataset to a pandas DataFrame.
dataset_df = pd.DataFrame(dataset['train'])

embedding_model = SentenceTransformer("thenlper/gte-small")

# Input: string.
# Output: list of floats.


def get_embedding(text):
    if not text.strip():
        print("Attempted to get embedding for empty text.")
        return []

    embedding = embedding_model.encode(text)

    return embedding.tolist()

dataset_df["embedding"] = dataset_df["text"].apply(get_embedding)

dataset_df["embedding"]

def get_mongo_client(mongo_uri):
    """Establish connection to the MongoDB."""
    try:
        client = pymongo.MongoClient(mongo_uri)
        print("Connection to MongoDB successful!")
        return client
    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection failed: {e}")
        return None

# Environment variables in Google Colaboratory.
# https://medium.com/@parthdasawant/how-to-use-secrets-in-google-colab-450c38e3ec75
load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
if not mongo_uri:
    print("MONGO_URI not set in environment variables")

#mongo_client = get_mongo_client(mongo_uri)

"""# Ingest data into MongoDB.
db = mongo_client["songs"]
# Reference to MongoDB collection
collection = db["songs_collection"]"""

st.write("Hello World!")