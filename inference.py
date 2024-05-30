from transformers import pipeline

eminem_pipe = pipeline("text-generation", model="huggingartists/eminem")
drake_pipe = pipeline("text-generation", model="huggingartists/drake")
snoop_pipe = pipeline("text-generation", model="huggingartists/snoop-dogg")

def eminem_generator(sentence : str):
    return eminem_pipe(sentence)

def drake_generator(sentence : str):
    return drake_pipe(sentence)

def snoop_generator(sentence : str):
    return snoop_pipe(sentence)