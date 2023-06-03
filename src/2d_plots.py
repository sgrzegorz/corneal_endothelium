import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable

from src.utils import path_root

name = 'median'

csv_path = path_root('result_with_sda',name , 'results.csv')
aggregate_by = {'fitness': np.mean, 'dice': np.mean, 'jaccard': np.mean, 'acc': np.mean}

df = pd.read_csv(csv_path)
print(f'------------- wszystkie razem ----------------')
df = df.groupby(['method', 'id'],as_index=False).agg(aggregate_by)
# df = df.sort_values('fitness', ascending=False)
df['r'] = [int(params.split('_')[0]) for params in df.id ]
df['param1'] = [int(params.split('_')[1]) for params in df.id ]
# df = df.sort_values('id_numeric', ascending=False)

# new_row = {'param1':4,'r':12,  'fitness':0.9}
# df = df.append(new_row,ignore_index=True)

result = df.pivot(index='r', columns='param1', values='fitness')


# result = result.interpolate(method='pad', limit=2)



# M = result.iloc[:,:].values.max()
# labels = result.iloc[:,:].applymap(lambda v: str(v) if v == M else '')


# sns.heatmap(result, fmt="",cmap="coolwarm", annot=labels, annot_kws={'fontsize':4})


ax = plt.subplot()
# image = ax.imshow(result, cmap='coolwarm', interpolation='bilinear')
image = ax.imshow(result, cmap='coolwarm')
plt.ylabel('R')
plt.xlabel('param1')

divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(image, cax=cax)



plt.show()


# import numpy as np
# import seaborn as sns
# import matplotlib.pylab as plt
#
# uniform_data = np.random.rand(10, 12)
# ax = sns.heatmap(uniform_data, linewidth=0.5)
# plt.show()

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