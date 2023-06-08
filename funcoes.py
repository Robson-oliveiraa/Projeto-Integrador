from sys import stdout
from time import sleep
from os import system

def text(txt):
    for letra in list(txt):
        print(letra, end = '')
        stdout.flush()
        sleep(0.05)
    sleep(0.05)
    print(end = '\n')

def toLoad(text, str, times):
    for i in range(3):
        for i in range(times):
            points = str*i
            print(text, points)
            sleep(0.4)
            system('cls')