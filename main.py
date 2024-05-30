from dotenv import load_dotenv
import os
import pandas as pd
# pip install llama-index llama-index-experimental
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import *
from pdf import drake_engine
from add_doc import search_json_
from llama_index.core import SimpleDirectoryReader
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI

load_dotenv()


drake_path = os.path.join("data", "drake_lyrics.csv")
drake_df = pd.read_csv(drake_path)

kendrick_path = os.path.join("data", "kendrick_lyrics.csv")
kendrick_df = pd.read_csv(kendrick_path)


# First model for queries / verbose shows the model's thinking
drake_query_engine = PandasQueryEngine(df=drake_df, verbose=False, instruction_str=instruction_str)
drake_query_engine.update_prompts({"pandas_prompt":new_prompt})

kendrick_query_engine = PandasQueryEngine(df=kendrick_df, verbose=False, instruction_str=instruction_str)
kendrick_query_engine.update_prompts({"pandas_prompt":new_prompt})


# Add in hugging face model - text generation inference
# Use a pipeline as a high-level helper

# tools that the LLM can use
    
tools = [
    
    note_engine,
    artist_engine,
    song_engine,
    read_JSON,
    eminem_rapping_engine,
    drake_rapping_engine,
    snoop_rapping_engine,
    QueryEngineTool(query_engine=drake_query_engine, metadata=ToolMetadata(
        name="drake_songs",
        description="this gives information on drake's song lyrics, show entire lyrics when asked")),
    QueryEngineTool(query_engine=kendrick_query_engine, metadata=ToolMetadata(
        name="kendrick_songs",
        description="this gives information on kendrick's song lyrics, show entire lyrics when asked")),
    QueryEngineTool(query_engine=drake_engine, metadata=ToolMetadata(
        name="drake_wiki_data",
        description="this gives information on drake's history and his career"))
]

def add_file(file_path):
    # Read the content of the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Create a temporary directory and write the content to a file
    temp_dir = os.path.join(os.getcwd(), "temp_dir")
    os.makedirs(temp_dir, exist_ok=True)
    temp_file_path = os.path.join(temp_dir, "temp_file.txt")

    with open(temp_file_path, 'w', encoding='utf-8') as temp_file:
        temp_file.write(content)

    # Convert the content into a SimpleDirectoryReader object
    reader = SimpleDirectoryReader(temp_dir)
    document = reader.load_data()

    # Create a new tool for the SimpleDirectoryReader
    query_engine = document.create_query_engine(verbose=False)
    metadata = ToolMetadata(
        name="text_file_reader",
        description="this reads and queries the content of a provided text file"
    )

    text_file_tool = QueryEngineTool(query_engine=query_engine, metadata=metadata)

    # Add the new tool to the tools list
    tools.append(text_file_tool)

llm = OpenAI(model="gpt-4-turbo")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)
"""
while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)
"""

def RAGquery(prompt):
    return agent.query(prompt)
# use another LLM to search songs and feed it to the main LLM
