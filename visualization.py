
import seaborn as sns
import matplotlib.pyplot as plt

def plot_travel_history(df):
    plt.figure(figsize=(12,12))
    sns.scatterplot(data=df, x='latitude', y='longitude', hue='id')
    plt.legend(bbox_to_anchor=[1, 1])
    plt.title('Travel History Graph', {'fontsize': 20, 'color':'red'})
    plt.savefig('Travel History Graph.png')
    plt.show()
