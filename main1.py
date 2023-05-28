import os

import numpy as np
import pandas as pd
from tqdm import tqdm

from main import  get_pairs
from src.dirs import extract_file_id
from src.utils import path_root

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
        return self.tp / self._white_pixels(self.img_gt.get_image())

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

class Statistics:
    # wylicza pandas table, dla wszystkich metryk fita
    def __init__(self):
        pass

class StatisticsView:
    # pokazuje odpowiednio wyfiltrowane widoki ze Statistics
    def __init__(self):
        pass


def get_dataset(file_id):
    file_id = int(file_id)
    if file_id < 100:
        raise Exception('Unknown file ')
    if file_id < 200:
        return 'yg'
    elif file_id < 300:
        return 'bs'
    elif file_id < 400:
        return 'jgs'
    elif file_id < 500:
        return 'ar'
    else:
        raise Exception('Unknown file ')

def generate_fit(gt_dir,generated_dir,df,method, subdir_name,columns):
    pairs = get_pairs(gt_dir, generated_dir)
    for (gen_img,gt_img) in tqdm(pairs):
        metric = get_metric(gt_img, gen_img)
        file_id = extract_file_id(gen_img.filename)
        dataset = get_dataset(file_id)
        row = pd.DataFrame([[method,subdir_name,file_id,dataset,metric.fitness(),metric.dice(),metric.jaccard(),metric.acc()]],columns=columns)
        df = pd.concat([df,row],ignore_index=True)
    return df
        # df.append({'method': method, 'id': subdir, 'dice' : metric.dice(),'jaccard' : metric.jaccard(),'acc' : metric.acc(),'fitness' : metric.fitness()},ignore_index = True)


def _subdirs(path):
    return [(f.path,f.name) for f in os.scandir(path) if f.is_dir()]

def generate_fits(method,generated_dir,csv_path):
    gt_dir = path_root('data', 'all')
    columns = ['method','id','file','dataset','fitness','dice','jaccard', 'acc']
    df = pd.DataFrame(columns = columns)
    for (subdir_path, subdir_name) in _subdirs(generated_dir):
        df = generate_fit(gt_dir, subdir_path,df, method,subdir_name,columns)
        df.to_csv(csv_path, index=False)
    return df


def process(method):
    # method = 'mean'
    generated_dir = path_root('result', method)
    csv_path = path_root('result',method,'results.csv')
    df = generate_fits(method,generated_dir,csv_path)
    df = pd.read_csv(csv_path)
    print(df)

# contrast 06.05,
