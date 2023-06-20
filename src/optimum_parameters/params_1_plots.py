import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from src.utils import load_dataset

from src.utils import path_root

def plot_optimum_1d(name,filtering):
    df = load_dataset(name,filtering)
    df = df.sort_values('r', ascending=False)

    plt.plot(df.r,df.fitness)
    plt.title(name)
    plt.scatter(list(df.r)[np.argmax(df.fitness)],np.max(df.fitness))
    plt.ylabel('dopasowanie')
    plt.xlabel('R')
    plt.savefig(path_root('plots','optimum','params_1',f'{filtering}_{name}'))
    plt.show()

for filtering in ['yg','bs','jgs']:
    for name in ['contrast','otsu']:
        plot_optimum_1d(name,filtering)
