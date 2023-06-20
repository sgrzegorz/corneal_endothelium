import os

import numpy as np
import pandas as pd


def root_dir():
  return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# path from project root
def path_root(*args):
  return os.path.abspath(os.path.join(root_dir(),*args))

# path from current dir
def path(*args):
  return os.path.abspath(os.path.join(*args))

def load_dataset(name, filtering=None, aggregate=True):
    csv_path = path_root('result', 'result_with_sda', name, 'results.csv')
    aggregate_by = {'fitness': np.mean, 'dice': np.mean, 'jaccard': np.mean, 'acc': np.mean}
    df = pd.read_csv(csv_path)
    if filtering is not None:
      df = df[df['dataset'] == filtering]
    if aggregate:
        df = df.groupby(['method', 'id','dataset'], as_index=False).agg(aggregate_by)
    df['r'] = [int(params.split('_')[0]) for params in df.id]
    df['param1'] = [float(params.split('_')[1]) for params in df.id]
    df['param2'] = [float(params.split('_')[2]) for params in df.id]

    return df