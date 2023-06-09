# -*- coding: utf-8 -*-
"""Daeguro_Hackathon_DBSCAN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17SWQx8W9xw6e7mLYWvu6zNBiuPkc1TQZ
"""

from sklearn import datasets
import pandas as pd

df_csv = pd.read_csv('/content/sample_data/(Final)yayaya4.csv')
df_csv

from sklearn.preprocessing import StandardScaler

standard_scaler = StandardScaler()
mall_scaled_df = pd.DataFrame(standard_scaler.fit_transform(df_csv), columns=df_csv.columns) # scaled된 데이터

#MinMaxScaler 적용
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

scaler.fit(df_csv)
df_scaled = scaler.transform(df_csv)

# nd.array형인 df_scaled를 dataframe으로 수정하는 코드
df_scaled = pd.DataFrame(df_scaled, columns = ['2030대 인구', '유동인구','대구로카페주문고객'])
df_scaled

df_scaled['총점'] = df_scaled['2030대 인구'] + df_scaled['유동인구']+ df_scaled['대구로카페주문고객']
df_scaled

#df_scaled['cluster'] = 0
df_scaled

from sklearn.cluster import DBSCAN
import matplotlib.pyplot  as plt
import seaborn as sns
plt.rc('font', family='Malgun Gothic')

# create model and prediction
model = DBSCAN(eps=0.1,min_samples=5)
predict = pd.DataFrame(model.fit_predict(df_scaled))
predict.columns=['predict']

# concatenate labels to df as a new column
r = pd.concat([df_scaled,predict],axis=1)

print(r)

#pairplot with Seaborn
sns.pairplot(r,hue='predict')
plt.show()

r.to_csv('/content/sample_data/DBSCAN_result.csv')