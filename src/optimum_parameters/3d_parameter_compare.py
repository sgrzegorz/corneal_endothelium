import numpy as np
from scipy.interpolate import RegularGridInterpolator
from src.utils import path_root, load_dataset
from matplotlib import cm
import matplotlib.pyplot as plt


def load_dataset_pivot(name,filtering=None):
    df = load_dataset(name,filtering)
    df['r'] = [int(params.split('_')[0]) for params in df.id ]
    df['param1'] = [int(params.split('_')[1]) for params in df.id ]
    return df.pivot(index='r', columns='param1', values='fitness')




def plot_wireframe(name,filtering):
    data = load_dataset_pivot(name,filtering)

    x = data.index
    y = data.columns
    data = data.to_numpy()


    xg, yg = np.meshgrid(x, y, indexing='ij')
    # data = ff(xg, yg)

    interp = RegularGridInterpolator((x, y), data, bounds_error=False, fill_value=None)

    print(interp((xg,yg)))


    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(projection='3d')

    # ax.scatter(xg.ravel(), yg.ravel(), data.ravel(),
    #
    #            s=60, c='k', label='data')



    X = np.linspace(start=5, stop=70, num=100)
    Y = np.linspace(start=0, stop=28, num=100)

    Xg, Yg = np.meshgrid(X, Y, indexing='ij')

    # interpolator
    print(interp((Xg, Yg)))
    Zg =  interp((Xg, Yg))
    ax.plot_wireframe(Xg, Yg,Zg, rstride=3, cstride=3,alpha=0.4, cmap=cm.coolwarm, label=f'{name}')
    ax.set_xlabel('r')
    ax.set_ylabel('param 1')
    ax.set_zlabel('dopasowanie')


    # surf = ax.plot_surface(Xg, Yg, Zg,  cmap=cm.coolwarm, shade=False)
    # surf.set_facecolor((0,0,0,0))


    index = np.argmax(Zg)
    ax.scatter(Xg.flatten()[index],Yg.flatten()[index],Zg.flatten()[index],color='black', s=65,label='maximum')


    # ground truth

    # ax.plot_wireframe(X, Y, ff(X, Y), rstride=3, cstride=3,
    #
    #                   alpha=0.4, label='ground truth')
    scatter(ax,name,filtering)
    title = f'{filtering}_{name}_3d'
    plt.title(title)
    plt.legend()
    plt.savefig(path_root('plots', 'optimum', title))
    plt.show()
    #
    # plt.imshow(interp((Xg, Yg)), cmap='hot')
    # plt.show()



def scatter(ax,name,filtering):
    df = load_dataset(name, filtering)
    df['param1'] = [int(params.split('_')[1]) for params in df.id]

    # fig = plt.figure(figsize=(12, 12))
    # ax = fig.add_subplot(projection='3d')

    sequence_containing_x_vals = df.r
    sequence_containing_y_vals = df.param1
    sequence_containing_z_vals = df.fitness

    ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals,label='punkty pomiarowe')


filtering  = 'yg'
for method in ['mean','median','midgrey','bernsen']:
    plot_wireframe(method, filtering)

