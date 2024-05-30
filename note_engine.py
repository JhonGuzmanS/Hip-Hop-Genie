import os
from llama_index.core.tools import FunctionTool
from test import abstract_songs
from pdf import load_artist
from add_doc import search_json_
from inference import *

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


# Function Tools for the LLM to use
note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="note_saver",
    description="this tool can save a text based note to a file for the user"
)

eminem_rapping_engine = FunctionTool.from_defaults(
    fn=eminem_generator,
    name="eminem_rapper",
    description="this tool returns a text generated response when giving a starter sentence, raps like eminem"
)

drake_rapping_engine = FunctionTool.from_defaults(
    fn=drake_generator,
    name="drake_rapper",
    description="this tool returns a text generated response when giving a starter sentence, raps like drake, use this as default if not specified or artist not found"
)

snoop_rapping_engine = FunctionTool.from_defaults(
    fn=eminem_generator,
    name="snoop_rapper",
    description="this tool returns a text generated response when giving a starter sentence, raps like snoop dogg"
)

artist_engine = FunctionTool.from_defaults(
    fn=load_artist,
    name="artist_saver",
    description="this tool saves information on a specific artist in JSON format"
)

song_engine = FunctionTool.from_defaults(
    fn=abstract_songs,
    name="song_saver",
    description="this tool gets song lyrics of any artist"
)

read_JSON = FunctionTool.from_defaults(
    fn=search_json_,
    name="JSON_reader",
    description="this tool reads JSON files when given the name of the desired song/artist. Useful for printing out lyrics and more"
)