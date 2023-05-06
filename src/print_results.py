import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from src.utils import path_root

def print_stats(dataset,csv_path,aggregate_by):
    print(f'------------- {dataset} ------------------')
    df = pd.read_csv(csv_path)
    df = df.loc[df['dataset']==dataset]
    df =df.groupby(['method' ,'id' ]).agg(aggregate_by)
    df = df.sort_values('fitness',ascending=False)

    print(df)
    print(f'Wyniki tylko dla zdjęć ze zbioru {dataset}')
    print('\n\n')
    return df.iloc[0, :]


def plot_with_bars(df,method):
    # [fitness, dice, jaccard, accuracy]
    barWidth = 0.15
    fig = plt.subplots(figsize=(12, 8))
    # yg =
    # bs =
    # ygs =
    # mean =

    # yg = [12, 30, 1, 8]
    # ygs = [28, 6, 16, 5]
    # bs = [29, 3, 24, 25]
    # mean = [21, 12, 12, 4]

    # Set position of bar on X axis
    br1 = np.arange(len(df.yg))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]

    # Make the plot
    plt.bar(br1, df.yg, color='r', width=barWidth,
            edgecolor='grey', label='yg')
    plt.bar(br2, df.ygs, color='g', width=barWidth,
            edgecolor='grey', label='ygs')
    plt.bar(br3, df.bs, color='b', width=barWidth,
            edgecolor='grey', label='bs')
    plt.bar(br4, df['mean'], color='y', width=barWidth,
            edgecolor='grey', label='mean')

    # Adding Xticks
    plt.xlabel('method', fontweight='bold')
    plt.ylabel('value [%]', fontweight='bold')
    plt.xticks([r + 1.5 * barWidth for r in range(len(df.yg))],
               ['fitness', 'dice', 'jaccard', 'accuracy'])
    plt.title(method,fontsize=20)
    plt.legend()
    plt.savefig(path_root('plots',method))
    plt.show()


def process_method(method):

    csv_path = path_root('result',method,'results.csv')
    aggregate_by = {'fitness': np.mean, 'dice': np.mean, 'jaccard': np.mean,'acc': np.mean}


    df = pd.read_csv(csv_path)
    print(f'------------- wszystkie razem ----------------')
    df =df.groupby(['method' ,'id' ]).agg(aggregate_by)
    df = df.sort_values('fitness',ascending=False)
    print('Wyniki dla wszystkich zdjęć, bez rozróżnienia na zbiory')
    print('\n\n')
    yg =[]
    bs = []
    ygs =[]
    df_all = None
    for i in {'yg','bs','ygs'}:
        df1 = print_stats(i,csv_path,aggregate_by)

        df_all = pd.concat([df_all, df1],axis=1)
    df_all = pd.concat([df_all,df_all.mean(axis=1)],axis=1)
    df_all.columns = ['yg', 'bs','ygs','mean']
    plot_with_bars(df_all,method)
    # df = pd.read_csv(csv_path)
    # aggregate_by = {'fitness': np.std, 'dice': np.std, 'jaccard': np.std,'acc': np.std}
    # df = df.groupby(['file' ]).agg(aggregate_by)
    # df = df.sort_values(by=['fitness'],ascending=False)
    # print(df)


    # plot_with_bars(yg, ygs, bs, mean)


process_method('contrast')