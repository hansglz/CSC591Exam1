import collections, json, time

import pandas as pd
import numpy as np
import networkx as nx

"""
EXPERIMENT GOAL
    Consider several types of "attacks", i.e., removing nodes or edges, 
    such attackes could be 'random' or 'organized' in any sense you define,
    then measure the connectivity of the resulting graphs.
    You can check if the resulting graph is connected or even measure the algebraic connectivity.

For the ER random graph (with parameter n and p):
    Removing each edge with probability 0<q<1 means the resulting graph is still ER random graph type,
    with new node-to-node connected probability of p*(1-q).
    You should figure out your own way to measure the resulting connective with that new n2n connected probability.

For the Power-Law graph:
    Simulate the preferential attachment model to generate random graph with power-law distribution,
    verify the results by plotting the CCDF of the degree distribution on a log-log scale,
    and then attack the nodes/edges randomly.
    If you choose to attack a node (which means remove the node with some probability),
    then all the edge associated with that node will also be removed.
    You should figure out your own way to judge the connectivity of the graph after different types of attack.    
"""

facebook = pd.read_csv(
    "data/facebook/facebook_combined.txt.gz",
    compression="gzip",
    sep=" ",
    names=["start_node", "end_node"],
)

def solution():
    fbGraph = nx.from_pandas_edgelist(facebook, "start_node", "end_node")
    randomGraph = nx.gnp_random_graph(4000, 0.25)
    powerlawGraph = nx.powerlaw_cluster_graph(4000, 2, 0.1)
    print("E-R random graph is connected? " + str(nx.is_connected(randomGraph)))
    print("Power-Law random graph is connected? " + str(nx.is_connected(powerlawGraph)))

    # degree_sequence = sorted([d for n, d in g.degree()], reverse=True)
    # degreeCount = collections.Counter(degree_sequence)
    # deg, cnt = zip(*degreeCount.items())
    # cs = np.cumsum(cnt)

solution()