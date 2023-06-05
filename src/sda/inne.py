import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from src.utils import path_root

def load_dataset2(name,directory='result_with_sda'):

    csv_path = path_root(directory,name , 'results.csv')
    aggregate_by = {'fitness': np.mean, 'dice': np.mean, 'jaccard': np.mean, 'acc': np.mean}

    df = pd.read_csv(csv_path)
    df = df.groupby(['method', 'id'],as_index=False).agg(aggregate_by)
    # df = df.sort_values('fitness', ascending=False)
    df['r'] = [int(params.split('_')[0]) for params in df.id ]
    df['param1'] = [int(params.split('_')[1]) for params in df.id ]
    df = df.sort_values(['r','param1'], ascending=True)
    return df

df = load_dataset2('mean','result_with_sda')

df_no = load_dataset2('mean','result_without_sda')

new_df = pd.merge(df, df_no,  how='inner',on=['r','param1'], suffixes=("_sda", "_normal"))
new_df = new_df.sort_values(['r', 'param1'], ascending=True)

print()
#
# plt.plot(df.id_numeric,df.fitness)
# plt.show()