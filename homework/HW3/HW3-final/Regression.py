#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:22:07 2020

@author: yingchenliu
"""

import numpy as np

class Regression():
    
    def __init__(self):
        self.params = {}
        
    def get_params(self):
        return self.params
    
    def set_params(self, **kwargs):
        self.params.update(kwargs)
        
    def fit(self, X, y):
        raise NotImplementedError
        
        
    def predict(self, X):
        raise NotImplementedError
    
    def score(self, X, y):
        
        raise NotImplementedError
    

class LinearRegression(Regression):
    
    # def __init__(self):
    #     Regression.__init__(self)
        
    def fit(self, X, y):
        """
        Parameters:
            X is n by p matrix
            y is n by 1 vector
        """
        n = X.shape[0]
        bias = np.ones((n,1))
        X = np.append(bias, X, axis=1)
       
        X_transpose = np.transpose(X) # (p+1)xn
        X_transpose_dot_X = X_transpose.dot(X) # (p+1)x(p+1)
        X_transpose_dot_y = X_transpose.dot(y) # (p+1)x1 
        
        tmp = np.linalg.pinv(X_transpose_dot_X)
        beta = tmp.dot(X_transpose_dot_y) # (p+1)x1
        
        self.params['coefficients'] = beta[1:]
        self.params['intercept'] = beta[0]
        
    def predict(self, X):
        """
        Parameters:
            X is n by p matrix
        """
        y_pred = np.dot(X, self.params['coefficients']) + self.params['intercept']
        return y_pred
    
    def score(self, X, y):
        """
        Parameters:
            X is n by p matrix
            y is n by 1 vector
        """
        SST = np.sum((y - np.mean(y))**2)
        SSE = np.sum((y - self.predict(X))**2)
        score = 1 - SSE/SST
        return score
    
    
class RidgeRegression(LinearRegression):
    # def __init__(self):
    #     Regression.__init__(self)
  
    def fit(self, X, y):
        """
        Parameters:
            X is n by p matrix
            y is n by 1 vector
        """
        n = X.shape[0]
        bias = np.ones((n,1))
        X = np.append(bias, X, axis=1)
        
        X_transpose = np.transpose(X) # (p+1)xn
        X_transpose_dot_X = X_transpose.dot(X) # (p+1)x(p+1)
        X_transpose_dot_y = X_transpose.dot(y) # (p+1)x1 
        
        a = X_transpose_dot_X.shape[0]
        
        gamma = self.params['alpha'] * np.identity(a)
        gamma_transpose = np.transpose(gamma)
        gamma_transpose_dot_gamma = gamma_transpose.dot(gamma)
        
        tmp =np.linalg.pinv(X_transpose_dot_X + gamma_transpose_dot_gamma)
        
        beta = tmp.dot(X_transpose_dot_y)
        
        self.params['coefficients'] = beta[1:]
        self.params['intercept'] = beta[0]
        
        
    def predict(self, X):
        """
        Parameters:
            X is n by p matrix
        """
        y_pred = np.dot(X, self.params['coefficients']) + self.params['intercept']
        return y_pred

        
        