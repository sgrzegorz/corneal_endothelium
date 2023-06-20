import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable
from src.utils import path_root, load_dataset




def plot_2d_heatmap(name, filtering):

    df = load_dataset(name,filtering)
    result = df.pivot(index='param1', columns='r', values='fitness')


    ax = plt.subplot()
    # image = ax.imshow(result, cmap='coolwarm', interpolation='bilinear')
    image = ax.imshow(result, cmap='hsv')
    plt.xlabel('R')
    plt.ylabel('param1')

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    plt.colorbar(image, cax=cax)
    plt.title(name)
    plt.savefig(path_root('plots', 'optimum', f'{filtering}_heatmap_{name}'), transparent=True)
    plt.show()

dataset  = 'yg'
for method in ['mean','median','midgrey','bernsen']:
    plot_2d_heatmap(method,dataset)

#
# import numpy as np
# import seaborn as sns
# import matplotlib.pylab as plt
#
# uniform_data = np.random.rand(10, 12)
# ax = sns.heatmap(uniform_data, linewidth=0.5)
# plt.show()
#
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
#
# data = np.where(np.random.rand(7, 10) < 0.2, np.nan, np.random.rand(7, 10) * 2 - 1)
# df = pd.DataFrame(data)
# annot_df = df.applymap(lambda f: f'{f:.1f}')
# fig, ax = plt.subplots(squeeze=False)
# sns.heatmap(
#     np.where(df.isna(), 0, np.nan),
#     ax=ax[0, 0],
#     cbar=False,
#     annot=np.full_like(df, "NA", dtype=object),
#     fmt="",
#     annot_kws={"size": 10, "va": "center_baseline", "color": "black"},
#     cmap=ListedColormap(['none']),
#     linewidth=0)
# sns.heatmap(
#     df,
#     ax=ax[0, 0],
#     cbar=False,
#     annot=annot_df,
#     fmt="",
#     annot_kws={"size": 10, "va": "center_baseline"},
#     cmap="coolwarm",
#     linewidth=0.5,
#     linecolor="black",
#     vmin=-1,
#     vmax=1,
#     xticklabels=True,
#     yticklabels=True)
# plt.show()