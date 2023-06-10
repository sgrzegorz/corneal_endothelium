import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from src.utils import path_root

name = 'contrast'

csv_path = path_root('result','result_with_sda',name , 'results.csv')
aggregate_by = {'fitness': np.mean, 'dice': np.mean, 'jaccard': np.mean, 'acc': np.mean}

df = pd.read_csv(csv_path)
print(f'------------- wszystkie razem ----------------')
df = df.groupby(['method', 'id'],as_index=False).agg(aggregate_by)
# df = df.sort_values('fitness', ascending=False)
df['id_numeric'] = [int(params.split('_')[0]) for params in df.id ]
df = df.sort_values('id_numeric', ascending=False)

plt.plot(df.id_numeric,df.fitness)
plt.show()