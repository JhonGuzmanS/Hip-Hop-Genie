import os
import json

def list_json_files(directory):
    """List all JSON files in the specified directory."""
    files = [f for f in os.listdir(directory) if f.endswith('.json')]
    return files

def load_json_file(file_path):
    """Load and return the content of a JSON file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def search_json_(filename):
    filename = filename + ".json"
    main_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Search for JSON files in the script directory
    json_files = list_json_files(main_directory)
    """Search for a specific JSON file by name in the specified directory."""
    json_files = list_json_files(main_directory)
    for file in json_files:
        if file == filename:
             data =  load_json_file(os.path.join(main_directory, file))
             return data.get('lyrics', "No lyrics")
    return None

def add_json(filename):
    return 0
