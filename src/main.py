import os
import numpy as np
from PIL import Image
import cv2

data = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','data'))
path_img_gt = os.path.join(data,'1_seg.png')
path_img = os.path.join(data,'1_s_max_SDAr6_bestfit.png')


def load(filename):
    image = Image.open(filename)
    return np.asarray(image,dtype=bool)


img_gt = cv2.imread(path_img_gt, cv2.IMREAD_GRAYSCALE)
img = cv2.imread(path_img, cv2.IMREAD_GRAYSCALE)


tp = 0
tn = 0
fp = 0
fn = 0
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
print(f'TP={tp}, FP={fp}')
print(f'FN={fn}, TN={tn}')
print(f'Accuracy: = {(tp+tn)/(tp+tn+fn+fp)}')

    # img_gt[x,y]

(img_gt==img).all()
#...

#
#
# import numpy as np
# from matplotlib import pylab as plt
#
# A = np.fromfile(filename1, dtype='int16', sep="")
# # A = A.reshape([1024, 1024])
# plt.imshow(A)

print()