#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 20:58:20 2020

@author: yingchenliu
"""
from sklearn import datasets
from sklearn.model_selection import train_test_split
from Regression import LinearRegression as lg
from Regression import RidgeRegression as rg
import numpy as np
import matplotlib.pyplot as plt



dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)

model1 = lg()
model2 = rg()

alphas = np.linspace(10e-2, 10, 100)
model1_scores = []
model2_scores = []
for alpha in alphas:
    model1.fit(X_train, y_train)
    score1 = model1.score(X_test, y_test)
    model1_scores.append(score1)
    
    model2.set_params(alpha=alpha)
    model2.fit(X_train, y_train)
    score2 = model2.score(X_test, y_test)
    model2_scores.append(score2)


log_alphas = np.log(alphas)
plt.figure(figsize=(10,8))
plt.plot(alphas, model1_scores,lw=2, label='Linear Regression')
plt.plot(alphas, model2_scores,lw=2,label='Ridge Regression')
# plt.xticks(alphas, size=15)
plt.title("plot of R-squared score vs. alpha values", size=20)
plt.xlabel("alpha",size=15)
plt.ylabel("score",size=15)
plt.legend()
plt.xscale("log")
plt.show()