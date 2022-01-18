from time import sleep
import sys

def slowprint(text : str):
    for char in f"{text}\n":
        sys.stdoutwrite(char)
        sys.stdout.flush()
        sleep(0.1)