from sys import stdout
from time import sleep
from os import system

def Text(Text):
    for letra in list(Text):
        print(letra, end = '')
        stdout.flush()
        sleep(0.05)
    sleep(0.05)
    print(end = '\n')
    system('cls')