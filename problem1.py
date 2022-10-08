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

def plot(data,filename):
    """ Plot Distribution """
    plt.plot(range(len(data)),data,'bo')
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('Freq')
    plt.xlabel('Degree')
    plt.savefig(filename + '_distribution.eps')
    plt.clf()

    """ Plot CDF """
    s = float(data.sum())
    cdf = data.cumsum(0)/s
    plt.plot(range(len(cdf)),cdf,'bo')
    plt.xscale('log')
    plt.ylim([0,1])
    plt.ylabel('CDF')
    plt.xlabel('Degree')
    plt.savefig(filename + '_cdf.eps')
    plt.clf()

    """ Plot CCDF """
    ccdf = 1-cdf
    plt.plot(range(len(ccdf)),ccdf,'bo')
    plt.xscale('log')
    plt.yscale('log')
    plt.ylim([0,1])
    plt.ylabel('CCDF')
    plt.xlabel('Degree')
    plt.savefig(filename + '_ccdf.eps')
    plt.clf()

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
plt.loglog(deg, cs, 'bo')
plt.title("Cumulative Distribution plot loglog")
plt.ylabel("Sample with value > Degree")
plt.xlabel("Degree")
plt.show()
plt.clf()

plt.semilogy(deg, cs, 'bo')
plt.title("Cumulative Distribution plot semi-log")
plt.ylabel("Sample with value > Degree")
plt.xlabel("Degree")
plt.show()
plt.clf()

plt.plot(deg, cs, 'bo')
plt.title("Cumulative Distribution plot linear-linear")
plt.ylabel("Sample with value > Degree")
plt.xlabel("Degree")
plt.show()
plt.clf()

# edgelist_file = sys.argv[1]

# """ Load graph """
# G = nx.read_edgelist(edgelist_file, nodetype=int, create_using=nx.DiGraph())
#
# """ To sparse adjacency matrix """
# M = nx.to_scipy_sparse_matrix(G)
#
# indegrees = M.sum(0).A[0]
# outdegrees = M.sum(1).T.A[0]
# indegree_distribution = np.bincount(indegrees)
# outdegree_distribution = np.bincount(outdegrees)

# plot(indegree_distribution, edgelist_file, 'indegree')
# plot(outdegree_distribution, edgelist_file, 'outdegree')