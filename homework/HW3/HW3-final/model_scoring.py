#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:36:22 2020

@author: yingchenliu
"""
from sklearn import datasets
from sklearn.model_selection import train_test_split
from Regression import LinearRegression as lg
from Regression import RidgeRegression as rg

dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)

alpha = 0.1

if __name__ == "__main__":
    model1 = lg()
    model2 = rg()
    
    model2.set_params(alpha=alpha)
    
    models = [model1, model2]
    
    for model in models:
        model.fit(X_train, y_train)
        print("==================================")
        print(model.score(X_test, y_test))
        print(model.get_params())
        
