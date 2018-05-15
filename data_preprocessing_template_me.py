# -*- coding: utf-8 -*-

#Data Preprocessing

#Import Libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing Dataset
dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,-1].values

#Taking care of missing Data

from sklearn.preprocessing import Imputer  #import of the class
imputer = Imputer(missing_values = 'NaN',strategy = 'mean',axis = 0) #Creating the object
imputer = imputer.fit(X[:,1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])




