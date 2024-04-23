import networkx as nx
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('data/MBTA_Rapid_Transit_Stop_Distances.csv')

graph = nx.Graph()

# pos = nx.spring_layout(graph)
# nx.draw_networkx_edges(graph,pos=pos)
edges = []
for index, row in df.iterrows():
  tup = (row['from_stop_name'],row['to_stop_name'])
  if tup in edges: pass
  else: edges.append(tup)
stops = df['from_stop_name'].unique()
graph.add_nodes_from(stops)
graph.add_edges_from(edges)
print(nx.shortest_path(graph,source='Copley',target='Airport'))


pos = nx.spring_layout(graph)
nx.draw_networkx_nodes(graph,pos=pos,node_size=0.01)
nx.draw_networkx_edges(graph,pos=pos)
plt.show()