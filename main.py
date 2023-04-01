import os
import numpy as np
from PIL import Image
import cv2
from src.dirs import get_pairs
from src.utils import path_root, path
import pickle

# data = os.path.abspath(os.path.join(os.path.dirname(__file__), '', 'data'))
# path_img_gt = os.path.join(data,'1_seg.png')
# path_img = os.path.join(data,'1_s_max_SDAr6_bestfit.png')


def load(filename):
    image = Image.open(filename)
    return np.asarray(image,dtype=bool)


class Metric:
    def __init__(self,tp,fp,fn,tn):
        self.tp = tp
        self.fp = fp
        self.fn = fn
        self.tn = tn

    def dice(self):
        return (2*self.tp) / (2*self.tp + self.fn + self.fp)

    def jaccard(self):
        return self.tp / (self.tp + self.fn + self.fp)

    def acc(self):
        return (self.tp + self.tn) / (self.tp + self.tn + self.fn + self.fp)


def get_metric(gt_img, gen_img):
    img_gt = cv2.imread(gt_img.path(), cv2.IMREAD_GRAYSCALE)
    img = cv2.imread(gen_img.path(), cv2.IMREAD_GRAYSCALE)

    tp = 0
    tn = 0
    fp = 0
    fn = 0
    # TODO pewnie można przyspieszyć przez nakładanie na siebie masek
    for (x,y), value in np.ndenumerate(img_gt):
        if img_gt[x,y] == 255:
            if img[x,y] == 255:
                tp +=1
            elif img[x,y] == 0:
                fn +=1
            else:
                raise Exception('1')
        elif img_gt[x,y] == 0:
            if img[x,y] == 0:
                tn +=1
            elif img[x,y] == 255:
                fp +=1
            else:
                raise Exception('2')
    # print(f'TP={tp}, FP={fp}')
    # print(f'FN={fn}, TN={tn}')
    return Metric(tp,fp,fn,tn)

class Fit:
    def __init__(self, gt_dir,generated_dir):
        self.gt_dir =  gt_dir
        self.generated_dir = generated_dir
        self.metrics = []
        self.gen_files = []
        self.gt_files = []

    def save(self):
        self.calc_mean()
        with open(path(self.generated_dir,'fit'),'wb') as output_file:
            pickle.dump(self,output_file)

    @staticmethod
    def load(filepath):
        with open(path(filepath,'fit'),'rb') as input_file:
            return pickle.load(input_file)
        raise FileNotFoundError

    def calc_mean(self):
        self.mean_acc = np.mean(np.array([ metric.acc() for metric in self.metrics]))
        self.mean_jaccard = np.mean(np.array([metric.jaccard() for metric in self.metrics]))
        self.mean_dice = np.mean(np.array([metric.dice() for metric in self.metrics]))




def generate_fit(gt_dir,generated_dir):
    pairs = get_pairs(gt_dir, generated_dir)
    fit = Fit(gt_dir, generated_dir)
    for (gt_img, gen_img) in pairs:
        metric = get_metric(gt_img, gen_img)
        fit.metrics.append(metric)
        fit.gt_files.append(gt_img)
        fit.gen_files.append(gen_img)

        print(metric.acc(), metric.dice(), metric.jaccard())

    fit.save()


if __name__ == '__main__':
    gt_dir = path_root('data','yg')
    generated_dir = path_root('result', 'bernsen')
    generate_fit(gt_dir,generated_dir)


