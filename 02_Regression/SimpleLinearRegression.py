# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Simple Linear Regression

#Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing Dataset
dataset = pd.read_csv('Salary_Data.csv')

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#splitting the dataset into the Training set and th Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 1/3, random_state = 0)

#Feature Sacalimg
"""from sklearn.preprocessing import StandardScaler
sc_X =StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

#Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predicting the Test set results
y_pred = regressor.predict(X_test)

#Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience ( Training set)')
plt.xlabel('Years of Experians')
plt.ylabel('Salary')
plt.show()

