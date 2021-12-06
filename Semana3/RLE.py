# https://www.pythonpool.com/run-length-encoding-python/
import numpy as np


def runLengthEncoding(fonte):
    comp = ""
    i = 0
    while i < len(fonte):
        if i < len(fonte) - 2 and fonte[i] == fonte[i+1] == fonte[i+2]:
            cont = 1
            while fonte[i] == fonte[i+1]:
                cont += 1
                i += 1
            comp += "@" + fonte[i] + str(cont)
        else:
            comp += fonte[i]
        i += 1
    return comp
