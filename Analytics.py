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
        self.tableDict = {}

    def preprocessDf(self):
        self.df.fillna(0)
    
    def my_best_mlp_tuned(self,x_train_scaled,x_test_scaled,y_train,y_test,param_grid):
  
        # Define the model
        model = MLPClassifier(n_iter_no_change=20)

        # Create a GridSearchCV object

        grid_search = GridSearchCV(model, param_grid,scoring='accuracy', cv=5, verbose = 3,n_jobs=-1) 

        # Fit the GridSearchCV object
        grid_search.fit(x_train_scaled, y_train)

        # Print the best hyperparameters
        #print("Best hyperparameters:", grid_search.best_params_)

        # Evaluate the best model on the test set
        accuracy = grid_search.score(x_test_scaled, y_test)
        print("MLP accuracy:", accuracy)


        # Get the best estimator
        best_model = grid_search.best_estimator_

        # Use the best model to make predictions
        predictions = best_model.predict(x_test_scaled)

        return accuracy
    def model_summary(self,model,x,y): #x = features, y = class label
    # Train the model
        #model.fit(X_train, y_train)

    # Predict on the test set
        y_pred = model.predict(x)

    # Evaluate the model
        accuracy = accuracy_score(y, y_pred)
        #print(f"Accuracy: {accuracy}")

    # Example of predicting probabilities for each class
        probabilities = model.predict_proba(x)
        print("Probabilities for each class:", probabilities)
    
    #  dfy is the y_test
    def my_best_logreg_tuned(self,x_test,dfy,param_grid):
        logit = LogisticRegression(multi_class='multinomial',penalty=None, max_iter=50) # no regularization as indicated by parameter penalty
        model_logit = logit.fit(self.x_train_scaled, self.y_train)
        
        self.model_summary(model_logit,self.x_train_scaled,self.y_train)

        self.model_summary(model_logit,self.x_test_scaled,self.y_test)
        clf = GridSearchCV(model_logit,param_grid = param_grid, cv = 5, verbose=True,n_jobs=-1)
        clf
        df1 = np.nan_to_num(x_test)
        dfy = np.nan_to_num(dfy)
        best_clf = clf.fit(df1,dfy)
        best_clf.best_estimator_
        score = best_clf.score(df1,dfy);
        # Print the best hyperparameters
        #print("Best hyperparameters:", best_clf.best_params_)
        #print(f'Log Regression Test Accuracy - : {score:.3f}')
        
        return score
    
    '''K-nearest Neighbor Model'''

    def my_best_knn_tuned(self,x_train_scaled,x_test_scaled,y_train,y_test):
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
        self.knn_accuracy = accuracy_score(y_test, y_pred)
        #print("Accuracy:", self.knn_accuracy)
        #print('best parameters ',clf_knn.best_params_)
        #print('K nearest Neighbors best validation score ', clf_knn.best_score_)
   
        return self.knn_accuracy
    
    def createSaveTable(self,feature):
        d = {
        'Model':['MLP','Logistic Regression','KNN'],
    '   Test Accuracy': [self.accuracy,self.best_clf,self.knn_accuracy]
        }
        self.tableDict[feature] = pd.DataFrame(data=d)
    
    def displayResultsTable(self):
        """ d = {
        'Model':['MLP','Logistic Regression','KNN'],
    '   Test Accuracy': [self.accuracy,self.best_clf,self.knn_accuracy]
        }
        self.table_single = pd.DataFrame(data=d) """
        for key in self.tableDict:
            print("*************************************************")
            print(f"\t\tResults for {key}")
            print(self.tableDict[key])

