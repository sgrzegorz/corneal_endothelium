from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from src.utils import load_dataset, path_root



def plot_unknown_3(name,filtering):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    df = load_dataset(name,filtering)

    # x = np.random.standard_normal(100)
    # y = np.random.standard_normal(100)
    # z = np.random.standard_normal(100)
    # c = np.random.standard_normal(100)

    img = ax.scatter(df.r, df.param1, df.param2, c=df.fitness, cmap='hsv')
    ax.set_xlabel('r')
    ax.set_ylabel('param1')
    ax.set_zlabel('param2')
    maximum = df[df.fitness == df.fitness.max()]
    ax.scatter(maximum.r, maximum.param1, maximum.param2, color='black', s=85, label='maximum')
    fig.colorbar(img,pad=0.13)

    title = f'{filtering}_{name}_4d'
    plt.title(title)
    plt.legend()

    plt.savefig(path_root('plots', 'optimum','params_3', title))
    plt.show()


for filtering in ['yg','bs','jgs']:
    for name in ['phansalkar','niblack','sauvola']:
        plot_unknown_3(name, filtering)
