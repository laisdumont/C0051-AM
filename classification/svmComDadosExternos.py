import pandas as pd
from sklearn.svm import SVC  
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_validate
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold # KFold Class.
from sklearn import metrics
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv('datasets/dadosCom2Classes.csv')
# Separando os atributos das classes
x = df.iloc[:,:-1].values
y = (df.iloc[:,-1:].values).ravel()

min_max_scaler = MinMaxScaler()
x = min_max_scaler.fit_transform(x)

# kfold  = KFold(n_splits=5, shuffle=True)
clf = SVC()
# clf = SVC(kernel='rbf',cache_size=200,C=1,degree=3)
# clf.fit(x, y)  
# print(clf.predict([[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]]))
# a = cross_val_predict(estimator=clf,X=x, y=y, cv=5)
a = cross_val_score(estimator=clf,X=x, y=y, cv=2)
print(a)
print(metrics.accuracy_score(y, a))
print(metrics.confusion_matrix(y, a))
# print(x)