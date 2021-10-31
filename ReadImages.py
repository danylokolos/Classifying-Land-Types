# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 21:55:54 2021

@author: Danylo
"""

""" Script to Read in Images, Output CSV with Processed Data for ML """


import os
import numpy as np
#import matplotlib.pyplot as plt
import imageio
import csv
from heapq import merge
import pickle


### get file list
a = os.getcwd()
b = os.path.dirname(a)
imagepath = b + '\EOBrowser-Images-PNG-L2A\SingleBandImages'
imagelist= os.listdir(imagepath)

### read images, make massive 3D matrix (height, width, depth)
count = 0
for x in imagelist:
    print(x)
    if count == 0:
        im = imageio.imread(imagepath + '\\' + imagelist[count])
        fullim = np.zeros((im.shape[0],im.shape[1],len(imagelist)),dtype=np.uint8)
        fullim[:,:,count] = im
    else:
        im = imageio.imread(imagepath + '\\' + imagelist[count])
        fullim[:,:,count] = im
    count= count + 1
fullim.shape
pickle.dump(fullim,open("fullim.pkl","wb"))
    
### find median value of each group of pixels
smoothsize = 20 # num of pixels in X and Y

#resize image to match scaling
tmpX = fullim.shape[0] % smoothsize
tmpY = fullim.shape[1] % smoothsize
fullimr = np.delete(fullim,range(-tmpX,0),0)
fullimr = np.delete(fullimr,range(-tmpY,0),0)

# new output matrix
procim = np.zeros((int(fullimr.shape[0]/smoothsize),int(fullimr.shape[1]/smoothsize),len(imagelist)),dtype=np.uint8)
for ii in range(0,procim.shape[0]):
    print('Loop',ii+1,'of',procim.shape[0])
    for jj in range(0,procim.shape[1]):
        for kk in range(0,procim.shape[2]):
            procim[ii,jj,kk] = np.median(fullimr[range((ii*smoothsize),(ii+1)*smoothsize),range(jj*smoothsize,(jj+1)*smoothsize),kk])
procim.shape
     
# test if image makes sense                                
image = imageio.imwrite('imageB12.png',procim[:,:,11])
        
### output csv file
f = open('FullImageDataset.csv','w+',newline='')
writer = csv.writer(f)
header = ['ImageX','ImageY','Band01','Band02','Band03','Band04','Band05','Band06','Band07','Band08','Band8A','Band09','Band11','Band12']
writer.writerow(header)
for ii in range(0,procim.shape[0]):
    for jj in range(0,procim.shape[1]):
        data = [ii+1,jj+1] 
        #data2 = procim[ii,jj,:]
        data.extend(procim[ii,jj,:])
        writer.writerow(data)
f.close()





# output csv for Machine Learning
              

"""    
    if count == 0:
        im = imageio.imread(imagepath + '\\' + imagelist[0])
    else:
        im = [im,imageio.imread(imagepath + '\\' + imagelist[0])]
    print(im.shape)
    count = count + 1
    
"""


#imageslist= os.listdir(imagespath)

#images_plt = [plt.imread(imageslist)]



#images = np.array(images_plt)



"""
print(imageslist[0])




imagespath = Users\Danylo\Documents\Education-2021-SAIT-MachineLearning\Assignments\Assignment01-SatelliteImageryLandCalssification\EOBrowser-Images-PNG-L2A\SingleBandImages
filelist = os.listdir(imagespath)


a = 1
b = (3,4,5,6)


print(filelist)


"""