
from sklearn.cluster import DBSCAN

def get_infected_name(df, input_name):
    
    epsilon = 0.0018288
    model = DBSCAN(eps=epsilon, min_samples=2, metric='haversine').fit(df[['latitude', 'longitude']])
    df['cluster'] = model.labels_.tolist()
    cluster_id_lst = df['cluster'].unique()

    
    infected = []
    for i in cluster_id_lst:
        if i != -1:
            f = df[df['cluster'] == i]
            names = list(f.iloc[:, 0])
            for j in names:
                if j not in infected:
                    if j != input_name:
                        infected.append(j)

    if len(infected) == 0:
        return 'No one came in contact with the patient.'
    elif len(infected) == 1:
        return f"{infected[0]} had come in contact with the patient."
    else:
        return f"The following people came in contact with the patient: {', '.join(infected)}"
