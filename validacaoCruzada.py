import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import StratifiedKFold
from sklearn.svm import SVC  
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from matplotlib import pyplot as plt
df = pd.read_csv('datasets/dadosProntos.csv')

# Separando os atributos das classes
x = df.iloc[:,:-1].values
y = df.iloc[:,-1:].values.ravel()
# print("Matrz de Atributos", x, sep='\n')
# print("--------------------------------------------------")
# print("Classes", y, sep='\n')

# a = cross_validate(estimator=any,X=x, y=y, cv=5)
accuracy = []
folds = StratifiedKFold(5)
# for i in range(1,10,2):
foldaccuracy = []
for train_index, test_index in folds.split(x, y):
        #print(train_index)
        #print(test_index)
        nn = RandomForestClassifier( )
        nn.fit(x[train_index],y[train_index])
        predicted = nn.predict(x[test_index])
        #print(sklearn.metrics.confusion_matrix(classes[test_index],predicted))
        foldaccuracy.append(metrics.accuracy_score(y[test_index],predicted))
        plt.figure(figsize=(20,20))
        tree.plot_tree(nn.estimators_[0], feature_names=x[train_index], filled=True)
#print(foldaccuracy)
accuracy.append(foldaccuracy)
print(accuracy)