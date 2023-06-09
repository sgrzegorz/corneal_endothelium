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
        return np.sum(image == 255)

    def fitness(self):
        return self.tp / self._white_pixels(self.img_gt.get_image())

    def information(self):
        a =  f" dice: {self.dice():.3f}, jaccard {self.jaccard():.3f}, accuracy {self.acc():.3f},  {self.fitness():.3f}"
        return a

def get_metric(gt_img, pred_img):
    gt = gt_img.get_image()
    pred = pred_img.get_image()
    if gt is None or pred is None:
        return None

    negative = 0
    positive = 255
    # tp = 0
    # tn = 0
    # fp = 0
    # fn = 0
    # for (x,y), value in np.ndenumerate(gt):
    #     if gt[x,y] == positive:
    #         if pred[x,y] == positive:
    #             tp +=1
    #         elif pred[x,y] == negative:
    #             fn +=1
    #         else:
    #             raise Exception('1')
    #     elif gt[x,y] == negative:
    #         if pred[x,y] == negative:
    #             tn +=1
    #         elif pred[x,y] == positive:
    #             fp +=1
    #         else:
    #             raise Exception('2')
    # print(tp,tn,fp,fn)

    tp = np.sum(np.logical_and(pred == positive, gt == positive))
    tn = np.sum(np.logical_and(pred == negative, gt == negative))
    fp = np.sum(np.logical_and(pred == positive, gt == negative))
    fn = np.sum(np.logical_and(pred == negative, gt == positive))
    # print(tp,tn,fp,fn)
    # print('-------------')

    # print(f'TP={tp}, FP={fp}')
    # print(f'FN={fn}, TN={tn}')
    return Metric(tp,fp,fn,tn,gt_img,pred_img)


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

def generate_fit(gt_dir,generated_dir,df,method, subdir_name,columns,disable):
    pairs = get_pairs(gt_dir, generated_dir)
    new_rows = pd.DataFrame([],columns=columns)
    for (gen_img,gt_img) in tqdm(pairs,disable=disable):
        file_id = extract_file_id(gen_img.filename)

        exists = df.loc[(df['method'] == method) & (df['id'] == subdir_name) & (df['file'] == file_id)].any().all()
        if not exists:
            dataset = get_dataset(file_id)
            metric = get_metric(gt_img, gen_img)
            if metric is None:
                continue
            row = pd.DataFrame([[method,subdir_name,file_id,dataset,metric.fitness(),metric.dice(),metric.jaccard(),metric.acc()]],columns=columns)
            new_rows = pd.concat([new_rows,row],ignore_index=True)
    return new_rows


def _subdirs(path):
    return [(f.path,f.name) for f in os.scandir(path) if f.is_dir()]

def generate_fits(method,generated_dir,csv_path,disable):
    gt_dir = path_root('data', 'all')
    columns = ['method','id','file','dataset','fitness','dice','jaccard', 'acc']
    df = pd.DataFrame(columns = columns)
    try:
        # df = pd.read_csv(csv_path)
        df = pd.DataFrame(columns=columns)

    except FileNotFoundError:
        print('Csv file was not found')
        exit(1)

    for (subdir_path, subdir_name) in _subdirs(generated_dir):
        new_rows = generate_fit(gt_dir, subdir_path,df, method,subdir_name,columns,disable)
        df = pd.concat([df,new_rows],ignore_index=True)
    return df


def process_to_csv(method, dir='result_with_sda',disable=False):
    generated_dir = path_root(dir, method)
    csv_path = path_root(dir,method,'results.csv')
    df = generate_fits(method,generated_dir,csv_path,disable)
    df.to_csv(csv_path, index=False)
    print(f'{method} finished.')

if __name__ == '__main__':
    process_to_csv('niblack','result_with_sda',disable=False)