import os
from dotenv import load_dotenv
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader
from llama_index.readers.genius import GeniusReader
from lyricsgenius import Genius
from llama_index.core.tools import QueryEngineTool, ToolMetadata


load_dotenv()


CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
genius = Genius(os.environ.get("GENIUS_ACCESS_TOKEN"), timeout=10, retries=3)
loader = GeniusReader(CLIENT_SECRET)

def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )
    
    return index

def load_artist(artist_name, songs, prompt):
    while True:
        try:
            documents = loader.load_artist_songs(artist_name, songs=3)
            break
        except:
            pass
    index = VectorStoreIndex.from_documents(documents)
    engine = index.as_query_engine()
    return engine.query(prompt)


pdf_path = os.path.join("data", "Drake_wiki.pdf")
drake_pdf = PDFReader().load_data(file=pdf_path)
drake_index = get_index(drake_pdf, "drake")
drake_engine = drake_index.as_query_engine()
