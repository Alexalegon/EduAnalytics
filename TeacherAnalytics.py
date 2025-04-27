from Analytics import Analytics
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

class TeacherAnalytics(Analytics):
    def __init__(self,trainingFname,testingFname):
        super().__init__()
        # read data and convert to panda data frame
        self.df = pd.read_csv(trainingFname, sep=',', na_values=['?'])
        self.df_test = pd.read_csv(testingFname, sep=",", na_values=['?'])
        self.featureList = ['Age','Gender','US Educated','Years of Experience']
        self.preprocessDf()
        self.labelEncode()
        self.runAnalytics()
        

    def runAnalytics(self):
        for item in self.featureList:
            self.setupTrainTest(item)
            self.runMlpTuned()
            self.runLogregTuned()
            self.runKNNTuned()
            self.createSaveTable(item)
        self.displayResultsTable()

    def labelEncode(self):
        label_encoder = preprocessing.LabelEncoder()
        self.df['Age']= label_encoder.fit_transform(self.df['Age'])
        self.df['Age'].unique()

        self.df['Gender']= label_encoder.fit_transform(self.df['Gender'])
        self.df['Gender'].unique()

        self.df['Years of Experience']= label_encoder.fit_transform(self.df['Years of Experience'])
        self.df['Years of Experience'].unique()

        self.df['Teacher Rating']= label_encoder.fit_transform(self.df['Teacher Rating'])
        self.df['Teacher Rating'].unique()

        self.df['US Educated']= label_encoder.fit_transform(self.df['US Educated'])
        self.df['US Educated'].unique()
       

        self.df_test['Age']= label_encoder.fit_transform(self.df_test['Age'])
        self.df_test['Age'].unique()
       
        self.df_test['Gender']= label_encoder.fit_transform(self.df_test['Gender'])
        self.df_test['Gender'].unique()

        self.df_test['Years of Experience']= label_encoder.fit_transform(self.df_test['Years of Experience'])
        self.df_test['Years of Experience'].unique()
        

        self.df_test['Teacher Rating']= label_encoder.fit_transform(self.df_test['Teacher Rating'])
        self.df_test['Teacher Rating'].unique()

        self.df_test['US Educated']= label_encoder.fit_transform(self.df_test['US Educated'])
        self.df_test['US Educated'].unique()
      
    
    def setupTrainTest(self,feature):
        # scale data
        self.x_train = np.array(self.df[feature].to_list()).reshape(-1,1)
        self.x_test = np.array(self.df_test[feature].to_list()).reshape(-1,1)
        self.y_train = np.array(self.df['Teacher Rating'].to_list()).reshape(-1,1)
        self.y_test = np.array(self.df_test['Teacher Rating'].to_list()).reshape(-1,1)
        self.scaler = StandardScaler()
        self.x_train_scaled = self.scaler.fit_transform(self.x_train)
        self.x_test_scaled = self.scaler.transform(self.x_test)

    def runMlpTuned(self):
        param_grid= {
            'max_iter':[100,250],
            'hidden_layer_sizes': [(10,2),(20,2),(50,20),(100,100)]
        }
        self.accuracy = self.my_best_mlp_tuned(self.x_train_scaled,self.x_test_scaled,
                                          self.y_train,self.y_test,param_grid)
        
    def runLogregTuned(self):
        param_grid = [
            {
            'solver':['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'],
            }
        ]
        self.best_clf = self.my_best_logreg_tuned(self.x_test,self.df_test['Teacher Rating'],param_grid)

    def runKNNTuned(self):
        self.knn_accuracy = self.my_best_knn_tuned(self.x_train_scaled,self.x_test_scaled,
                                                   self.y_train,self.y_test)