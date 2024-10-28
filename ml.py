import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt

%matplotlib inline

df = pd.read_json('newdataset.json')
df

plt.figure(figsize=(12,12))
sns.scatterplot(data=df, x='latitude', y='longitude', hue='id')
plt.legend(bbox_to_anchor = [1, 1])
plt.title('Travel History Graph', {'fontsize': 20, 'color':'red'})
plt.savefig('Travel History Graph')
plt.show();

sns.jointplot(x='latitude', y='longitude', data=df, color='red', kind='kde')

sns.boxplot(x='id', y='longitude', data=df, palette='coolwarm')
plt.tight_layout() 

from sklearn.cluster import DBSCAN
def get_infected_name(input_name):
    # 6 feet to kilometers
    epsilon =0.0018288
    model = DBSCAN(eps=epsilon, min_samples=2, metric='haversine').fit(df[['latitude', 'longitude']])
    df['cluster'] = model.labels_.tolist()
    cluster_id_lst = df['cluster'].unique()

    # appending all the infected peoples who came in contact with patient.
    infected = []
    for i in cluster_id_lst:
        if i!=-1:
            f = df[df['cluster']==i]
            names = list(f.iloc[:,0])
            for j in names:
                if j not in infected:
                    if j!=input_name:
                        infected.append(j)
    if len(infected)==0:
        print('No one came in contact with the patient.')
    elif len(infected)==1:
        print("%s had come in contact with the patient."%infected[0])
    else:
        print("The following people came in contact with the patient:- \n",infected)

get_infected_name('Alice')

z = df[df['cluster']==0] # cluster-0 peoples
z


lat =  z.iloc[0,2]-z.iloc[1,2]
long = z.iloc[0,3]-z.iloc[1,3]
dist = np.sqrt((lat*lat)+(long*long))
print(dist, "km")

get_infected_name('Bob')