import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add edges with weights
G.add_edge('A', 'B', weight=1.5)
G.add_edge('A', 'C', weight=2.5)
G.add_edge('B', 'C', weight=3.0)

# Generate a planar layout for the graph
pos = nx.planar_layout(G)

# Draw the graph with node labels
nx.draw_planar(G, pos, with_labels=True, node_color='lightblue', node_size=500)

# Draw edge labels to show weights
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show the plot
plt.show()
