import matplotlib.pyplot as plt
import networkx as nx

# Define the stops and routes
stops = ["Portorosa", "Vulcano", "Stromboli", "Salina", "Panarea", "Lipari", "Portorosa"]
distances = [18, 22, 17, 9, 12, 18]
colors = ["blue", "green", "red", "orange", "purple", "cyan"]

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges with distances
for i in range(len(stops) - 1):
    G.add_edge(stops[i], stops[i + 1], weight=distances[i], color=colors[i])

# Define positions for the nodes (circular layout for simplicity)
pos = nx.circular_layout(G)

# Draw the nodes
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="lightblue")

# Draw the edges with colors
edges = G.edges(data=True)
edge_colors = [edge[2]['color'] for edge in edges]
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, arrows=True, arrowsize=20)

# Draw the labels
nx.draw_networkx_labels(G, pos, font_size=10, font_color="black")
edge_labels = {(u, v): f"{d['weight']} NM" for u, v, d in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="black")

# Add title
plt.title("Marmalade-Style Maritime Routes Diagram")

# Save and show the diagram
plt.savefig("marmalade_chart.png")
plt.show()