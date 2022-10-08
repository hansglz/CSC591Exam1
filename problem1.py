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
    "data/facebook/facebook_combined.txt.gz",
    compression="gzip",
    sep=" ",
    names=["start_node", "end_node"],
)

twitch = pd.read_csv(
    "data/twitch/musae_ENGB_edges.csv",
    sep=",",
    names=["start_node", "end_node"]
)

github = pd.read_csv(
    "data/github/musae_git_edges.csv",
    sep=",",
    names=["start_node", "end_node"]
)

data = {'facebook': facebook, 'twitch': twitch, 'github': github}

def load_graph(data):
    g = nx.from_pandas_edgelist(data, "start_node", "end_node")
    degree_sequence = sorted([d for n, d in g.degree()], reverse=True)
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    cs = np.cumsum(cnt)
    return deg, cs

def question_a():
    for key in data:
        deg, cs = load_graph(data[key])
        # plt.loglog(deg, cs, 'bo')
        plt.plot(deg, cs, 'bo')
        plt.xscale('log')
        plt.yscale('log')
        plt.title("Cumulative Distribution plot log-log")
        plt.ylabel("Sample with value > Degree")
        plt.xlabel("Degree")
        # plt.show()
        plt.savefig("image/" + key + "_log-log")
        plt.clf()

        # plt.semilogy(deg, cs, 'bo')
        plt.plot(deg, cs, 'bo')
        plt.xscale('log')
        plt.title("Cumulative Distribution plot semi-log")
        plt.ylabel("Sample with value > Degree")
        plt.xlabel("Degree")
        # plt.show()
        plt.savefig("image/" + key + "_semi-log")
        plt.clf()

        plt.plot(deg, cs, 'bo')
        plt.xscale('linear')
        plt.yscale('linear')
        plt.title("Cumulative Distribution plot linear-linear")
        plt.ylabel("Sample with value > Degree")
        plt.xlabel("Degree")
        # plt.show()
        plt.savefig("image/" + key + "_linear-linear")
        plt.clf()

question_a()