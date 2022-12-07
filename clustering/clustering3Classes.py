import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('datasets/dadosTratados.csv')

df = df.drop(columns=['ip'])

kmeans = KMeans(n_clusters=3).fit(df)
pred = kmeans.predict(df)

df.insert(12,'classe',pred,True)

print(df.groupby('classe').count())
# print(df)
df.to_csv('datasets/dadosCom3Classes.csv', index=False)