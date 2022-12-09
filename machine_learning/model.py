import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from database.connection import client
from sklearn.feature_extraction import DictVectorizer

db = client.insurance.insurance.find({},
    {'_id':0, "id":0, "name":0})

insurance_data = pd.DataFrame(list(db))

# mengubah string di kolom sex, smoker, region menjadi int
insurance_data.replace({'sex':{'male':0,'female':1}}, inplace=True)

insurance_data.replace({'smoker':{'yes':0,'no':1}}, inplace=True)

insurance_data.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}}, inplace=True)

X = insurance_data.drop(columns='charges', axis=1)
Y = insurance_data['charges'].astype('float')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

insurance_model = LinearRegression()

insurance_model.fit(X_train, Y_train)

import pickle
with open('.\models\insurance_prediction.pickle', 'wb') as f:
    pickle.dump(insurance_model, f)

# prediction on training data
#training_data_prediction =insurance_model.predict(X_train)
#r2_train = metrics.r2_score(Y_train, training_data_prediction)

# prediction on test data
#test_data_prediction =insurance_model.predict(X_test)
#r2_test = metrics.r2_score(Y_test, test_data_prediction)