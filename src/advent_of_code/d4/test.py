import networkx as nx
import matplotlib.pyplot as plt

# Define the nodes and edges (you can modify this as needed)
nodes = [1, 2, 3, 4, 5, 6]
edges = [(1, 3), (1, 5), (2, 4), (3, 6), (4, 6)]

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
G.add_nodes_from(nodes)

# Add edges to the graph
G.add_edges_from(edges)

# Calculate positions for nodes in a stair-like layout
pos = {}
for i, node in enumerate(nodes):
    pos[node] = (i, i)

# Determine additional positions for edges to maintain horizontal and vertical connections
# for u, v in edges:
#     pos[v] = (pos[u][0], pos[v][1])

# Plot the graph
plt.figure(figsize=(8, 6))
nx.draw(
    G,
    pos=pos,
    with_labels=True,
    node_size=500,
    node_color="skyblue",
    font_weight="bold",
    arrows=True,
    connectionstyle="arc3, rad=0.5",  # Ensures edges are straight lines
)
plt.title(
    "Stair-like Representation of Nodes with Forward Edges (Arbitrary Nodes and Edges)"
)
plt.show()
