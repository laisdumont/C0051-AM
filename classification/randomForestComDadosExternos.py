import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import KFold # KFold Class.
from sklearn import metrics
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv('datasets/dadosCom3Classes.csv')

# Separando os atributos das classes
x = df.iloc[:,:-1].values
y = (df.iloc[:,-1:].values).ravel()

min_max_scaler = MinMaxScaler()
x = min_max_scaler.fit_transform(x)

kfold  = KFold(n_splits=5, shuffle=True)
clf = RandomForestClassifier()

a = cross_val_predict(estimator=clf,X=x, y=y, cv=5)
print(a)
print(metrics.accuracy_score(y, a))
# print(x)