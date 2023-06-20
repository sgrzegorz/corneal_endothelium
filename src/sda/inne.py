import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from src.utils import load_dataset
from src.utils import path_root

def load_dataset_2d_3d(name,directory='result_with_sda',two_params = True):

    df = load_dataset(name)
    if two_params:
        df['param1'] = [int(params.split('_')[1]) for params in df.id ]
    else:
        df['param1'] = [float(params.split('_')[1]) for params in df.id ]
        df['param2'] = [float(params.split('_')[2]) for params in df.id ]
    df = df.sort_values(['r','param1'], ascending=True)
    return df

method ='niblack'
two_params = False
df = load_dataset_2d_3d(method,'result_with_sda',two_params=two_params)
df_no = load_dataset_2d_3d(method,'result_without_sda',two_params=two_params)
new_df = pd.merge(df, df_no,  how='inner',on=['r','param1'], suffixes=("_sda", "_normal"))
new_df = new_df.sort_values(['r', 'param1'], ascending=True)

plt.bar(new_df.id_sda, new_df.fitness_sda - new_df.fitness_normal, color ='maroon',width = 0.4)

plt.title(method)
plt.ylabel('Polepszenie wyników po zastosowaniu SDA')

plt.savefig(path_root('plots','sda',f'sda_{method}'))
plt.show()

print(new_df)


# plt.plot(df.id_numeric,df.fitness)
# plt.show()