import pandas as pd
import pygal
from sklearn.cluster import DBSCAN
def contactTracing(dataFrame, inputName):
    #Check if name is valid
    assert (inputName in dataFrame['User'].tolist()), "User Doesn't exist"
    #Social distance
    safe_distance = 0.0018288 #6 feets in kilometers
    #Apply model, in case of larger dataset or noisy one, increase min_samples
    model = DBSCAN(eps=safe_distance, min_samples=2, metric='haversine').fit(dataFrame[['Latitude', 'Longitude']])
    #Get clusters found bt the algorithm 
    labels = model.labels_dataFrame['Cluster'] = model.labels_.tolist()
    #Add the clusters to the dataframe
    
    #Get the clusters the inputName is a part of
    inputNameClusters = set()
    for i in range(len(dataFrame)): 
        if dataFrame['User'][i] == inputName:
            inputNameClusters.add(dataFrame['Cluster'][i])
   #Get people who are in the same cluster as the inputName              
    infected = set()
    for cluster in inputNameClusters:
        if cluster != -1: #as long as it is not the -1 cluster
            namesInCluster = dataFrame.loc[dataFrame['Cluster'] == cluster, 'User'] #Get all names in the cluster
            for i in range(len(namesInCluster)):
              #locate each name on the cluster
                name = namesInCluster.iloc[i]
                if name != inputName: #Don't want to add the input to the results
                    infected.add(name)
    print("Potential infections are:",*infected,sep="\n")