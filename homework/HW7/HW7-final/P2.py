#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 23:25:38 2020

@author: yingchenliu
"""

import pandas as pd
import numpy as np
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer


# Part A: Create an SQL database called regression.sqlite 
db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")
cursor.execute("PRAGMA foreign_keys=1")

cursor.execute('''CREATE TABLE model_params (
               id INTEGER NOT NULL, 
               desc TEXT, 
               param_name TEXT, 
               value NUMERIC)''')

db.commit() # Commit changes to the database

cursor.execute('''CREATE TABLE model_coefs (
          id INTEGER NOT NULL, 
          desc TEXT, 
          feature_name TEXT, 
          value NUMERIC)''')

db.commit()

cursor.execute('''CREATE TABLE model_results (
          id INTEGER NOT NULL, 
          desc TEXT, 
          train_score NUMERIC, 
          test_score NUMERIC)''')

db.commit()


## Part B
## 1. Import additional libraries and load data
# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)

# get feature name
features_name = X.columns

## 2. Write a function to save data to the database
def save_to_database(model_id, model_desc, db, model, X_train, X_test, y_train, y_test):

    train_acc = model.score(X_train, y_train)
    val_acc = model.score(X_test, y_test)
    
    try:
        # connect data base
        sqliteConnection = sqlite3.connect(db)
        cursor = sqliteConnection.cursor()
        print('Connected to',db)
     
        insert_to_model_params  = '''INSERT INTO model_params (id, desc, param_name, value) VALUES(?, ?, ?, ?)'''
        insert_to_model_coefs= '''INSERT INTO model_coefs (id, desc, feature_name, value) VALUES(?, ?, ?, ?)'''
        insert_to_model_results = '''INSERT INTO model_results (id, desc, train_score, test_score) VALUES(?, ?, ?, ?)'''
        
        # insert params value into model_params
        for k,v in model.get_params().items():
            data_tuple = (model_id, model_desc, k, v)
            cursor.execute(insert_to_model_params, data_tuple)
            sqliteConnection.commit()
        print('Finished inserting into model_params.')
        
        # insert coefficient values into model_coefs
        for feature, value in zip(features_name, model.coef_[0]):
            data_tuple = (model_id, model_desc, feature, value)
            cursor.execute(insert_to_model_coefs, data_tuple)
            sqliteConnection.commit()
            
        # insert intercept value into model_coefs
        data_tuple = (model_id, model_desc, 'intercept', model.intercept_[0])
        cursor.execute(insert_to_model_coefs, data_tuple)
        sqliteConnection.commit()
        print('Finished inserting into model_coefs.')
        
        # insert results in to model_results
        data_tuple = (model_id, model_desc, train_acc, val_acc)
        cursor.execute(insert_to_model_results, data_tuple)
        sqliteConnection.commit()
        print('Finished inserting into model_results.')
        
        cursor.close()
        
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table:", error)
    finally:
        print("The SQLite connection is closed.\n")


## 3. Baseline logistic regression model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)  
print('Baseline logistic regression model\n-----------------------')
save_to_database(1, 'Baseline model', 'regression.sqlite', baseline_model, X_train, X_test, y_train, y_test)


## 4. Reduced logistic regression model
feature_cols = ['mean radius', 
                'texture error',
                'worst radius',
                'worst compactness',
                'worst concavity']

X_train_reduced = X_train[feature_cols]
X_test_reduced = X_test[feature_cols]

reduced_model = LogisticRegression(solver='liblinear')
reduced_model.fit(X_train_reduced, y_train)
print('Reduced logistic regression model\n-----------------------')
save_to_database(2, 'Reduced model', 'regression.sqlite', reduced_model, X_train_reduced, X_test_reduced, y_train, y_test)

## 5. Logistic regression model with L1 penalty
penalized_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
penalized_model.fit(X_train, y_train)
print('Logistic regression model with L1 penalty\n-----------------------')
save_to_database(3, 'L1 penalty model', 'regression.sqlite', penalized_model, X_train, X_test, y_train, y_test)


## Part C
print('\n\nid of the best model and the corresponding test score:\n-----------------------')
query = '''SELECT id FROM model_results ORDER BY test_score DESC LIMIT 1'''
best_model_id = cursor.execute(query).fetchall()
query = '''SELECT MAX(test_score) FROM model_results '''
best_validation_score = cursor.execute(query).fetchall()
print("Best model id: ", best_model_id[0][0])
print("Best validation score: ", best_validation_score[0][0])


print("\n\nFeature names and the corresponding coefficients of that model:\n-----------------------")
query = '''SELECT feature_name, value FROM model_coefs WHERE id = 3'''
result = cursor.execute(query).fetchall()
coef = []
intercept = []
for i in result:
    print(i[0],':', i[1])
    if i[0] == 'intercept':
        intercept.append(i[1])
    else:
        coef.append(i[1])

 
    
# Use the coefficients extracted from the best model to reproduce the test score (accuracy) of the best performing model 
test_model = LogisticRegression(solver='liblinear')
test_model.fit(X_train, y_train)

# Manually change fit parameters
test_model.coef_ = np.array([coef])
test_model.intercept_ = np.array([intercept])

test_score = test_model.score(X_test, y_test)
print(f'\n\nReproduced best validation score: {test_score}')


# ## display database

# def viz_tables(cols, query):
#     q = cursor.execute(query).fetchall()
#     framelist = dict()
#     for i, col_name in enumerate(cols):
#         framelist[col_name] = [row[i] for row in q]
#     return pd.DataFrame.from_dict(framelist)

# model_coefs_cols = [col[1] for col in cursor.execute("PRAGMA table_info(model_coefs)")]
# query = '''SELECT * FROM model_coefs'''
# print(viz_tables(model_coefs_cols, query))

# model_result_cols = [col[1] for col in cursor.execute("PRAGMA table_info(model_results)")]
# query = '''SELECT * FROM model_results'''
# print(viz_tables(model_result_cols, query))

# model_params_cols = [col[1] for col in cursor.execute("PRAGMA table_info(model_params)")]
# query = '''SELECT * FROM model_params'''
# print(viz_tables(model_params_cols, query))

db.commit()
db.close()