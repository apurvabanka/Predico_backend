import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import redis
# import seaborn as sns; sns.set()
import csv

r=redis.Redis()
#r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
df = pd.read_csv('apartment_data.csv')
# df=df['lat']*1000
#print(df.tail(10))
df.dropna(axis=0,how='any',subset=['lat','lon'],inplace=True)
# Variable with the Longitude and Latitude
X=df.loc[:,['names','lat','lon']]
#print(X.tail(10))
K_clusters = range(1,10)
kmeans = [KMeans(n_clusters=i) for i in K_clusters]
Y_axis = df[['lat']]
X_axis = df[['lon']]
score = [kmeans[i].fit(Y_axis).score(Y_axis) for i in range(len(kmeans))]
kmeans = KMeans(n_clusters = 5, init ='k-means++')
kmeans.fit(X[X.columns[1:3]]) # Compute k-means clustering.
X['cluster_label'] = kmeans.fit_predict(X[X.columns[1:3]])
centers = kmeans.cluster_centers_ # Coordinates of cluster centers.
labels = kmeans.predict(X[X.columns[1:3]]) # Labels of each point
X.head(10)
centers = kmeans.cluster_centers_
first_lat=centers[0][0]/10000000
first_lon=centers[0][1]/10000000
second_lat=centers[3][0]/10000000
second_lon=centers[3][1]/10000000
third_lat=centers[4][0]/10000000
third_lon=centers[4][1]/10000000
r.mset({"first_lat":first_lat,"first_lon":first_lon,
        "second_lat":second_lat,"second_lon":second_lon,
        "third_lat":third_lat,"third_lon":third_lon})
print(centers)



