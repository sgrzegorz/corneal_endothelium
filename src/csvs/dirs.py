import os

import cv2
from tqdm import tqdm

from src.utils import path
import re

class File:
    def __init__(self,id,filename,dirname):
        self.id = id
        self.filename = filename
        self.dirname = dirname

    def __str__(self):
        return f'{self.id} {self.filename} {self.dirname}'

    def path(self):
        return path(self.dirname,self.filename)

    def get_image(self):
        image = cv2.imread(self.path(), cv2.IMREAD_GRAYSCALE)
        if image is None:
            print(f'Image did not load correctly {self}')
        return image





def extract_file_id(filename):
    id = re.search('^(\d+)', filename)
    if id:
        return int(id.group(0))
    else:
        raise Exception("Unknown file format")

def get_full_paths(dir_name):
    files = []
    for filename in os.listdir(dir_name):
        if 'bestfit' in filename:
            id = extract_file_id(filename)
            files.append(File(id,filename,dir_name))

    return files

def get_pairs(gt_dir, generated_dir):
    gt_files = get_full_paths(gt_dir)
    generated_files = get_full_paths(generated_dir)

    pairs = []
    for generated_file in generated_files:
        for gt_file in gt_files:
            if generated_file.id == gt_file.id:
                pairs.append((generated_file, gt_file,))
    return pairs


# gt_dir = path_root('data','yg')
# generated_dir = path_root('result', 'bernsen')
# pairs = get_pairs(gt_dir,generated_dir)
#
# for pair in pairs:
#     print(pair[0],pair[1].path())