import numpy as np
from matplotlib import pyplot as plt

from src.utils import path_root


import pandas as pd

name = 'otsu'

csv_path = path_root('result','result_with_sda',name , 'results.csv')
aggregate_by = {'fitness': np.mean, 'dice': np.mean, 'jaccard': np.mean, 'acc': np.mean}

df = pd.read_csv(csv_path)
df = df.groupby(['method', 'id'],as_index=False).agg(aggregate_by)
df['R'] = [int(params.split('_')[0]) for params in df.id ]
df = df.sort_values('R', ascending=False)
plt.plot(df.R,df.fitness,label='użyto SDA')

csv_path = path_root('result','result_without_sda',name , 'results.csv')
df = pd.read_csv(csv_path)
df = df.groupby(['method', 'id'],as_index=False).agg(aggregate_by)
df['R'] = [int(params.split('_')[0]) for params in df.id ]
df = df.sort_values('R', ascending=False)
plt.plot(df.R,df.fitness, label = 'nie użyto SDA')
plt.legend()
plt.xlabel('R')
plt.ylabel('dopasowanie')
plt.title(name)
plt.savefig(path_root('plots',f'{name}_sda_test'))

plt.show()