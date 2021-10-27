# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 21:42:24 2021

@author: Danylo
"""

""" Script to Read in Validation Data Coordinates, Image matrix, output Validation/Test Data for ML """

%reset -f

import pickle
import csv
import numpy as np


# load saved 12 band image
fullim = pickle.load(open("fullim.pkl","rb"))
fullim.shape

# load validation coordinates
filename = "DatasetTrainValidateCoordinates.csv"
fields = []
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
        

# output csv file for ML
smoothsize = 20
f = open('ValidationTestDataset.csv','w+',newline='')
writer = csv.writer(f)
header = ['Category','LandType','ImageX','ImageY','Band01','Band02','Band03','Band04','Band05','Band06','Band07','Band08','Band8A','Band09','Band11','Band12']
writer.writerow(header)
for ii in range(0,len(rows)):
    data = [rows[ii][1],rows[ii][2]]
    data.extend([rows[ii][3],rows[ii][4]])
    for iBand in range(0,fullim.shape[2]):
        tmp = np.median(fullim[range(int(rows[ii][4]),int(rows[ii][4])+smoothsize),range(int(rows[ii][3]),int(rows[ii][3])+smoothsize),iBand])
        data.append(tmp)
    writer.writerow(data)
f.close()

# output csv file for ML, bigger x4
smoothsize = 10
f = open('ValidationTestDatasetBigger.csv','w+',newline='')
writer = csv.writer(f)
header = ['Category','LandType','ImageX','ImageY','Band01','Band02','Band03','Band04','Band05','Band06','Band07','Band08','Band8A','Band09','Band11','Band12']
writer.writerow(header)
for ii in range(0,len(rows)):
    data = [rows[ii][1],rows[ii][2]]
    data1 = data[:]
    data2 = data[:]
    data3 = data[:]
    data4 = data[:]    
    data1.extend([int(rows[ii][3]),int(rows[ii][4])])
    data2.extend([int(rows[ii][3]),smoothsize+int(rows[ii][4])])
    data3.extend([smoothsize+int(rows[ii][3]),int(rows[ii][4])])
    data4.extend([smoothsize+int(rows[ii][3]),smoothsize+int(rows[ii][4])])
    for iBand in range(0,fullim.shape[2]):
        tmp1 = np.median(fullim[range(int(rows[ii][4]),int(rows[ii][4])+smoothsize),range(int(rows[ii][3]),int(rows[ii][3])+smoothsize),iBand])
        tmp2 = np.median(fullim[range(int(rows[ii][4])+smoothsize,int(rows[ii][4])+smoothsize*2),range(int(rows[ii][3]),int(rows[ii][3])+smoothsize),iBand])
        tmp3 = np.median(fullim[range(int(rows[ii][4]),int(rows[ii][4])+smoothsize),range(int(rows[ii][3])+smoothsize,int(rows[ii][3])+smoothsize*2),iBand])
        tmp4 = np.median(fullim[range(int(rows[ii][4])+smoothsize,int(rows[ii][4])+smoothsize*2),range(int(rows[ii][3])+smoothsize,int(rows[ii][3])+smoothsize*2),iBand])
        data1.append(tmp1)
        data2.append(tmp2)
        data3.append(tmp3)
        data4.append(tmp4)

    writer.writerow(data1)
    writer.writerow(data2)
    writer.writerow(data3)
    writer.writerow(data4)

f.close()