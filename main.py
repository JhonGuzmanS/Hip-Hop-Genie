from dotenv import load_dotenv
import os
import pandas as pd
# pip install llama-index llama-index-experimental
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from pdf import drake_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI

load_dotenv()


pop_path = os.path.join("data", "drake_data.csv")
pop_df = pd.read_csv(pop_path)

#print(pop_df.head())

# First model for queries
pop_query_engine = PandasQueryEngine(df=pop_df, verbose=True, instruction_str=instruction_str)
pop_query_engine.update_prompts({"pandas_prompt":new_prompt})

# Add in hugging face model - text generation inference

#pop_query_engine.query("How many songs are there") # returns the query output
# tools that the LLM can use
tools = [
    note_engine,
    QueryEngineTool(query_engine=pop_query_engine, metadata=ToolMetadata(
        name="drake_data",
        description="this gives information on drake's song lyrics")),

    QueryEngineTool(query_engine=drake_engine, metadata=ToolMetadata(
        name="drake_wiki_data",
        description="this gives information on drake's history and his career"))
]

llm = OpenAI(model="gpt-3.5-turbo-0613")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)