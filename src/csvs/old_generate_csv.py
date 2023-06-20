import os
import numpy as np
import pandas as pd
from tqdm import tqdm
from PIL import Image
import cv2
from src.csvs.dirs import get_pairs
from src.utils import path_root, path
import pickle

# data = os.path.abspath(os.path.join(os.path.dirname(__file__), '', 'data'))
# path_img_gt = os.path.join(data,'1_seg.png')
# path_img = os.path.join(data,'1_s_max_SDAr6_bestfit.png')


def load(filename):
    image = Image.open(filename)
    return np.asarray(image,dtype=bool)


class Metric:
    def __init__(self,tp,fp,fn,tn,img_gt,img):
        self.tp = tp
        self.fp = fp
        self.fn = fn
        self.tn = tn
        self.img_gt = img_gt
        self.img = img

    def dice(self):
        return (2*self.tp) / (2*self.tp + self.fn + self.fp)

    def jaccard(self):
        return self.tp / (self.tp + self.fn + self.fp)

    def acc(self):
        return (self.tp + self.tn) / (self.tp + self.tn + self.fn + self.fp)

    def _white_pixels(self,image):
        count=0
        for (x, y), value in np.ndenumerate(image):
            if image[x, y] == 255:
                count+=1
        return count

    def fitness(self):
        return self.tp / self._white_pixels(self.gt_img.get_image())

    def information(self):
        a =  f" dice: {self.dice():.3f}, jaccard {self.jaccard():.3f}, accuracy {self.acc():.3f},  {self.fitness():.3f}"
        return a


def get_metric(gt_img, gen_img):
    img_gt = gt_img.get_image()
    img = gen_img.get_image()

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
                fp +=1
            else:
                raise Exception('1')
        elif img_gt[x,y] == 0:
            if img[x,y] == 0:
                tn +=1
            elif img[x,y] == 255:
                fn +=1
            else:
                raise Exception('2')
    # print(f'TP={tp}, FP={fp}')
    # print(f'FN={fn}, TN={tn}')
    return Metric(tp,fp,fn,tn,gt_img,gen_img)

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
        self.mean_fitness = np.mean(np.array([metric.fitness() for metric in self.metrics]))

    def get_means(self):
        return f" dice: {self.mean_dice:.3f}, jaccard: {self.mean_jaccard:.3f}, accuracy: {self.mean_acc:.3f}, fitness: {self.mean_fitness:.3f}"




def generate_fit(gt_dir,generated_dir):
    pairs = get_pairs(gt_dir, generated_dir)
    fit = Fit(gt_dir, generated_dir)
    for (gt_img, gen_img) in tqdm(pairs):
        metric = get_metric(gt_img, gen_img)
        fit.metrics.append(metric)

        metric.information();
        fit.gt_files.append(gt_img)
        fit.gen_files.append(gen_img)

        print(metric.information())

    fit.save()


def _subdirs(path):
    return [f.path for f in os.scandir(path) if f.is_dir()]

def generate_fits(gt_dir,generated_dir):
    for subdir in _subdirs(generated_dir):
        generate_fit(gt_dir, subdir)





if __name__ == '__main__':
    gt_dir = path_root('data','all')
    generated_dir = path_root('result', 'kch_snake')
    generate_fits(gt_dir, generated_dir)
    # generated_dir = path_root('result', 'contrast')
    # generated_dir = path_root('result', 'nibla')
    # generate_fit(gt_dir,generated_dir)






