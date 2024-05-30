from llama_index.core import PromptTemplate

instruction_str = """\
    1.Convert the query to executable Python code using  Pandas.
    2. The final line of code should be a Python expression that can be called with the 'eval()' function.
    3. The code should represent a solution to the query.
    4. PRINT ONLY THE EXPRESSION.
    6. Show ENTIRE string for 'lyrics' column
    """
    
new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is 'df'.
    This is the result of 'print(df.head())':
    {df_str}
    
    Follow these instructions:
    {instruction_str}
    Query: {query_str}
    
    Expression: """
)

context = """Purpose: The primary role of this agent is to assist users by providing accurate information on song lyrics and the artist, 
possibly interpreting what said artist would sing about and helping the user detect similarities between songs and artists."""