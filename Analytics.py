import numpy as np
import pandas as pd
import seaborn as sns; 
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import log_loss
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from array import array
import statistics
'''K-nearest Neighbor Model'''
from sklearn import preprocessing
from sklearn.utils import resample
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
import random

class Analytics:
    def __init__(self):
        print()
    
    def my_best_mlp_tuned(x_train_scaled,x_test_scaled,y_train,y_test,param_grid):
  
        # Define the model
        model = MLPClassifier(n_iter_no_change=20)

        # Create a GridSearchCV object

        grid_search = GridSearchCV(model, param_grid,scoring='accuracy', cv=5, verbose = 3,n_jobs=-1) 

        print("**************************")
        # Fit the GridSearchCV object
        grid_search.fit(x_train_scaled, y_train)

        # Print the best hyperparameters
        print("Best hyperparameters:", grid_search.best_params_)

        # Evaluate the best model on the test set
        accuracy = grid_search.score(x_test_scaled, y_test)
        print("MLP accuracy:", accuracy)


        # Get the best estimator
        best_model = grid_search.best_estimator_

        # Use the best model to make predictions
        predictions = best_model.predict(x_test_scaled)

        print('\n**********************************')
        return accuracy
    def model_summary(model,x,y): #x = features, y = class label
    # Train the model
        #model.fit(X_train, y_train)

    # Predict on the test set
        y_pred = model.predict(x)

    # Evaluate the model
        accuracy = accuracy_score(y, y_pred)
        print(f"Accuracy: {accuracy}")

    # Example of predicting probabilities for each class
        probabilities = model.predict_proba(x)
        print("Probabilities for each class:", probabilities)
    
    #  dfy is the y_test
    def my_best_logreg_tuned(x_test,dfy,param_grid):
        logit = LogisticRegression(multi_class='multinomial',penalty=None, max_iter=50) # no regularization as indicated by parameter penalty
        model_logit = logit.fit(x_train_scaled, y_train)
        print('*********************************\n')
        print('training')
        model_summary(model_logit,x_train_scaled,y_train)
        print('testing')
        model_summary(model_logit,x_test_scaled,y_test)
        clf = GridSearchCV(model_logit,param_grid = param_grid, cv = 5, verbose=True,n_jobs=-1)
        clf
        df1 = np.nan_to_num(x_test)
        dfy = np.nan_to_num(dfy)
        best_clf = clf.fit(df1,dfy)
        best_clf.best_estimator_
        score = best_clf.score(df1,dfy);
        # Print the best hyperparameters
        print("Best hyperparameters:", best_clf.best_params_)
        print(f'Log Regression Test Accuracy - : {score:.3f}')
        print('\n****************************************')
        return score
    
    '''K-nearest Neighbor Model'''

    def my_best_knn_tuned(x_train_scaled,x_test_scaled,y_train,y_test):
        # 5-fold cross validation
        k_grid = [k for k in range(1,100)] # list that contains differerent values of k (nearest neighbors)

        knn_grid={'n_neighbors':k_grid}
        knn_model = KNeighborsClassifier()
        clf_knn = GridSearchCV(knn_model, 
                    param_grid = knn_grid,
                    scoring = 'accuracy',
                    cv = 5, 
                    n_jobs = 4, #parallel processing to reduce computation time
                    return_train_score = True)
        clf_knn.fit(x_train_scaled,y_train)
        y_pred = clf_knn.predict(x_test_scaled)
        knn_accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy:", knn_accuracy)
        print('*********************************************\n')
        print('best parameters ',clf_knn.best_params_)
        print('K nearest Neighbors best validation score ', clf_knn.best_score_)
        print('\n************************************************')
        return knn_accuracy
    
