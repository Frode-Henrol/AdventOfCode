import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


edge_list = [((1,2), (2,3), 10), 
             ((3,5), (10,1), 5), 
             ((8,3), (6,1), 120)]


G = nx.Graph()
#G.add_edges_from(edge_list)
G.add_weighted_edges_from(edge_list)



# Create graph
G = nx.Graph()

# Add weighted edges
G.add_weighted_edges_from(edge_list)

# Visualize or analyze the graph
print(G.edges(data=True))  # Outputs edges with weights


print(nx.adjacency_matrix(G))

nx.draw_spring(G, with_labels=True)
#nx.draw_kamada_kawai(G, with_labels=True)

#print(nx.shortest_path(G,3,10))

plt.show()


