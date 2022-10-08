import collections

import pandas as pd
import numpy as np
import scipy as sp
import networkx as nx
import matplotlib.pyplot as plt
from random import randint
import sys
import networkx as nx
import matplotlib.pyplot as plt

facebook = pd.read_csv(
    "data/facebook_combined.txt.gz",
    compression="gzip",
    sep=" ",
    names=["start_node", "end_node"],
)

""" Load Graph """
G = nx.from_pandas_edgelist(facebook, "start_node", "end_node")
# M = nx.to_scipy_sparse_matrix(G)
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())
cs = np.cumsum(cnt)

# plt.loglog(deg, cs, 'bo')
plt.plot(deg, cs, 'bo')
plt.xscale('log')
plt.yscale('log')
plt.title("Cumulative Distribution plot log-log")
plt.ylabel("Sample with value > Degree")
plt.xlabel("Degree")
plt.show()
plt.clf()

# plt.semilogy(deg, cs, 'bo')
plt.plot(deg, cs, 'bo')
plt.xscale('log')
plt.title("Cumulative Distribution plot semi-log")
plt.ylabel("Sample with value > Degree")
plt.xlabel("Degree")
plt.show()
plt.clf()

plt.plot(deg, cs, 'bo')
plt.xscale('linear')
plt.yscale('linear')
plt.title("Cumulative Distribution plot linear-linear")
plt.ylabel("Sample with value > Degree")
plt.xlabel("Degree")
plt.show()
plt.clf()