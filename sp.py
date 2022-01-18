from time import sleep
from sys.stdout import write, flush

def slowprint(text : str):
    for char in f"{text}\n":
        write(char)
        flush()
        sleep(0.1)