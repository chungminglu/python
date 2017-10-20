# coding: utf-8
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import concurrent.futures
import os

def datagen(filename, destination):
    datagen = ImageDataGenerator(
            rotation_range=0.2,
            width_shift_range=0.2,
            height_shift_range=0.2,
            rescale=1./255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest')
    
    img = load_img(filename)
    x = img_to_array(img) 
    x = x.reshape((1,) + x.shape)
    filename = filename.split('/')[1]
    
    i = 0 #number of image generated
    for batch in datagen.flow(x, batch_size=1,
                          save_to_dir=destination, save_prefix=filename, save_format='jpg'):
        i += 1
        if i > 50:
            break  

photoDir = 'female_faces/'
photoList = os.listdir(photoDir)
direction = 'female_faces/'
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    for photo in photoList:
        try:
            filename = photoDir+photo
            executor.submit(datagen, filename, direction)
        except Exception as exc:
            print(exc)

