import inspect

from src.utils import load_dataset, path_root
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure



def load(methods,filtering='yg'):
    # methods = ['contrast', 'otsu', ... ]
    dfs = []
    for method in methods:
        dfs.append(load_dataset(method, filtering=filtering, aggregate=False))
    return dfs


def aggregat(df):
    aggregate_by = {'fitness': np.max}  # 'dice': np.max, 'jaccard': np.max, 'acc': np.max
    return df.groupby(['method', 'file'], as_index=False).agg(aggregate_by)


def describe(name):
    plt.xlabel("numer zdjęcia")
    plt.ylabel('dopasowanie')
    plt.savefig(path_root('plots', 'barplots', name))
    plt.show()


def bar_1_param(figsize):
    methods = ['contrast', 'otsu']
    dfs = load(methods)

    df1 = aggregat(dfs[0])

    N = df1.shape[0]
    ind = np.arange(N)
    width = 0.25
    plt.figure(figsize=figsize, dpi=80)
    bar1 = plt.bar(ind, df1.fitness, width, color='r')

    df1 = aggregat(dfs[1])
    bar2 = plt.bar(ind + width, df1.fitness, width, color='g')
    plt.xticks(ind + width / 2, [f'{i}' for i in range(1, 1 + N)])
    plt.legend((bar1, bar2), methods)
    plt.title('metody z jednym parametrem')
    describe(inspect.currentframe().f_code.co_name)


def bar_2_param(figsize):
    methods = ['median', 'midgrey','bernsen','mean']
    dfs = load(methods)

    df1 = aggregat(dfs[0])

    N = df1.shape[0]
    ind = np.arange(N)
    width = 0.15
    plt.figure(figsize=figsize, dpi=80)
    bar1 = plt.bar(ind, df1.fitness, width, color='r')

    df1 = aggregat(dfs[1])
    bar2 = plt.bar(ind + width, df1.fitness, width, color='g')

    df1 = aggregat(dfs[2])
    bar3 = plt.bar(ind + 2*width, df1.fitness, width, color='b')

    df1 = aggregat(dfs[3])
    bar4 = plt.bar(ind + 3*width, df1.fitness, width, color='y')

    plt.xticks(ind + 1.5*width , [f'{i}' for i in range(1, 1 + N)])
    plt.legend((bar1,bar2 ,bar3, bar4), methods)
    plt.title('metody z dwoma parametrami')

    describe(inspect.currentframe().f_code.co_name)


def bar_3_param(figsize):
    methods = ['sauvola', 'phansalkar','niblack']
    dfs = load(methods)

    df1 = aggregat(dfs[0])

    N = df1.shape[0]
    ind = np.arange(N)
    width = 0.15
    plt.figure(figsize=figsize, dpi=80)
    bar1 = plt.bar(ind, df1.fitness, width, color='r')

    df1 = aggregat(dfs[1])
    bar2 = plt.bar(ind + width, df1.fitness, width, color='g')

    df1 = aggregat(dfs[2])
    bar3 = plt.bar(ind + 2*width, df1.fitness, width, color='b')

    plt.xticks(ind + width , [f'{i}' for i in range(1, 1 + N)])
    plt.legend((bar1,bar2 ,bar3), methods)
    plt.title('metody z trzema parametrami')
    describe(inspect.currentframe().f_code.co_name)


figsize = (19,6,)
bar_1_param(figsize)
bar_2_param(figsize)
bar_3_param(figsize)
