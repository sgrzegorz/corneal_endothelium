import pickle

from main import Fit, Metric
from src.utils import path, path_root
# import pyplot.plt as plt

fit = Fit.load(path_root('result','bernsen'))

print(fit.mean_dice, fit.mean_acc, fit.mean_jaccard)
# plt.plot()
# plt.show()

print(fit)