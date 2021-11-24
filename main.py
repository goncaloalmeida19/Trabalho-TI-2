import matplotlib.pyplot as plt
import numpy as np


def hist(fonte, nome):
    ocorr = {}
    for j in fonte:
        if j not in ocorr:
            ocorr[j] = 1
        else:
            ocorr[j] += 1

    ocorr = list(ocorr.items())
    ocorr = dict(sorted(ocorr, key=lambda x: x[1], reverse=True))
    plt.bar(ocorr.keys(), ocorr.values())
    plt.title(nome)
    plt.show()
    return ocorr


# Função que devolve uma tabela com as probabilidades de ocorrência de cada elemento da tabela passada como argumento
def prob(ocorr):
    return ocorr / sum(ocorr)


# Função que passada uma tabela de probabilidades devolve a entropia
def entropia(p):
    p = p[p != 0]
    return -sum(p * np.log2(p))


file_names = ["bible.txt", "finance.csv", "jquery-3.6.0.js", "random.txt"]
for i in file_names:
    file = ""
    with open("dataset\\" + i, "r") as f:
        file = f.read()

    ocorr = hist(file, i)
    print("Entropia: {0:.4} bits/ símbolo".format(entropia(prob(np.array(list(ocorr.values()))))))
