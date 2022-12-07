import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('datasets/dadosCom3Classes.csv')

df.loc[df['classe'] == 2, 'classe'] = 1

print(df.groupby('classe').count())
df.to_csv('datasets/dadosCom2Classes.csv', index=False)