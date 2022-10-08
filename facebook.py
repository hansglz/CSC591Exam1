import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from random import randint

facebook = pd.read_csv(
    "data/facebook/facebook_combined.txt.gz",
    compression="gzip",
    sep=" ",
    names=["start_node", "end_node"],
)

G = nx.from_pandas_edgelist(facebook, "start_node", "end_node")

print("Number of nodes inside G: " + str(G.number_of_nodes()))
print("Number of edges inside G: " + str(G.number_of_edges()))
print("Is G connected? " + str(nx.is_connected(G)))

fig, ax = plt.subplots(figsize=(15, 9))
ax.axis("off")
plot_options = {"node_size": 10, "with_labels": False, "width": 0.15}
nx.draw_networkx(G, pos=nx.random_layout(G), ax=ax, **plot_options)

plt.show()