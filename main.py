import matplotlib.pyplot as plt


file_names = ["bible.txt", "finance.csv", "jquery-3.6.0.js","random.txt"]
for i in file_names:
    file = ""
    with open("dataset\\"+i, "r") as f:
        file = f.read()
    ocorr = {}
    for j in file:
        if j not in ocorr:
            ocorr[j] = 1
        else:
            ocorr[j] += 1
    ocorr = list(ocorr.items())
    ocorr = dict(sorted(ocorr, key=lambda x: x[1], reverse=True))
    plt.plot(list(ocorr.keys()),list(ocorr.values()))
    plt.title(i)
    plt.show()
