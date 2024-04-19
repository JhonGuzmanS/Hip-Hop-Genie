import os
from llama_index.core.tools import FunctionTool

note_file = os.path.join("data", "notes.txt")

# Can create any function/ return any type of data. 
# LLM can call the saved function

def save_note(note):
    if not os.path.exists(note):
        open(note_file, "w")
        
    with open(note_file, "a") as f:
        f.writelines([note + "\n"])
        
    # indicates/tells that the note was saved
    return "note saved"


note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="note_saver",
    description="this tool can save a text based note to a file for the user"
)
