from src.utils import load_dataset
import numpy as np
import matplotlib.pyplot as plt


methods = ['contrast', 'otsu','bernsen','mean','median','midgrey','niblack','phansalkar','sauvola']
dfs = []
for method in methods:
    dfs.append(load_dataset(method,filtering='yg'))


def bar_1_param():
    N = 4
    ind = np.arange(N)
    width = 0.25

    xvals = [8, 9, 2,1]
    bar1 = plt.bar(ind, xvals, width, color='r')

    yvals = [10, 20, 30,40]
    bar2 = plt.bar(ind + width, yvals, width, color='g')

    zvals = [11, 12, 13,14]
    bar3 = plt.bar(ind + width * 2, zvals, width, color='b')

    plt.xlabel("Dates")
    plt.ylabel('Scores')
    plt.title("metody z jednym parametrem")

    plt.xticks(ind + width, ['zdjęcie1', 'zdjęcie2', 'zdjęcie3','zdjęcie4'])
    plt.legend((bar1, bar2, bar3), ('contrast', 'otsu', 'mean','median'))
    plt.show()

print()