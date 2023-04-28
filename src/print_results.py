import numpy as np
import pandas as pd

from src.utils import path_root

csv_path = path_root('result','otsu','results.csv')
df = pd.read_csv(csv_path)
aggregate_by = {'fitness': np.mean, 'dice': np.mean, 'jaccard': np.mean,'acc': np.mean}


print(f'------------- wszystkie razem ----------------')
df =df.groupby(['method' ,'id' ]).agg(aggregate_by)

print(df)
print('Wyniki dla wszystkich zdjęć, bez rozróżnienia na zbiory')
print('\n\n')

def print_stats(dataset):
    print(f'------------- {dataset} ------------------')
    df = pd.read_csv(csv_path)
    df = df.loc[df['dataset']==dataset]
    df =df.groupby(['method' ,'id' ]).agg(aggregate_by)
    print(df)
    print(f'Wyniki tylko dla zdjęć ze zbioru {dataset}')
    print('\n\n')

for i in {'yg','bs','ygs','ar'}:
    print_stats(i)