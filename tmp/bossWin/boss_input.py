# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import numpy as np
import cv2
IMAGE_SIZE = 256

def resize_with_pad(image, height=IMAGE_SIZE, width=IMAGE_SIZE):
    def get_padding_size(image):
        h, w, _ = image.shape
        longest_edge = max(h, w)
        top, bottom, left, right = (0, 0, 0, 0)
        if h < longest_edge:
            dh = longest_edge - h
            top = dh // 2
            bottom = dh - top
        elif w < longest_edge:
            dw = longest_edge - w
            left = dw // 2
            right = dw - left
        else:
            pass
        return top, bottom, left, right

    top, bottom, left, right = get_padding_size(image)
    BLACK = [0, 0, 0]
    constant = cv2.copyMakeBorder(image, top , bottom, left, right, cv2.BORDER_CONSTANT, value=BLACK)
    resized_image = cv2.resize(constant, (height, width))
    return resized_image

images = []
labels = []
def traverse_dir(path):
    for file_or_dir in os.listdir(path):
        abs_path = os.path.abspath(os.path.join(path, file_or_dir))
        print(abs_path)
        if os.path.isdir(abs_path):  # dir
            traverse_dir(abs_path)
        else:                        # file
            if file_or_dir.endswith('.jpg'):
                image = read_image(abs_path)
                images.append(image)
                labels.append(path)
    return images, labels

def read_image(file_path):
    image = cv2.imread(file_path)
    image = resize_with_pad(image, IMAGE_SIZE, IMAGE_SIZE)
    return image

def test(ll):
    if str(ll).endswith('hsiung'):
        return 1
    elif str(ll).endswith('qqq'):
        return 2
    elif str(ll).endswith('tibame'):
        return 3                  
    else:
        return 0

def extract_data(path):
    images, labels = traverse_dir(path)
    images = np.array(images)

    # labels = np.array([1 if label.endswith('hsiung') 
                        # else 0 for label in labels])

    labels = np.array(list(map(test,labels)))
    return images, labels
