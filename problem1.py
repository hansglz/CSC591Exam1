import collections, json, time

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

def question_b():
    for key in data:
        print("Parsing data from: " + key)
        g = nx.from_pandas_edgelist(data[key], "start_node", "end_node")

        print("Start calculating eigen centrality for " + key + " dataset")
        tic = time.perf_counter()
        eigenCentrality = nx.eigenvector_centrality(g)
        toc = time.perf_counter()
        print(f"Calculate eigen centrality in {toc - tic:0.4f} seconds\n")

        print("Start calculating page rank centrality for " + key + " dataset")
        tic = time.perf_counter()
        pageRankCentrality = nx.pagerank(g)
        toc = time.perf_counter()
        print(f"Calculate page rank centrality in {toc - tic:0.4f} seconds\n")

        print("Start calculating betweenness centrality for " + key + " dataset")
        tic = time.perf_counter()
        # betweennessCentrality = nx.betweenness_centrality(g)
        toc = time.perf_counter()
        print(f"Calculate betweenness centrality in {toc - tic:0.4f} seconds\n")

        print("Start calculating closeness centrality for " + key + " dataset")
        tic = time.perf_counter()
        closenessCentrality = nx.closeness_centrality(g)
        toc = time.perf_counter()
        print(f"Calculate closeness centrality in {toc - tic:0.4f} seconds\n")

        sorted((v, f"{c:0.2f}") for v, c in eigenCentrality.items())
        sorted((v, f"{c:0.2f}") for v, c in pageRankCentrality.items())
        # sorted((v, f"{c:0.2f}") for v, c in betweennessCentrality.items())
        sorted((v, f"{c:0.2f}") for v, c in closenessCentrality.items())

        f = open("output/" + key + "_eigen_centrality.txt", "w")
        f.write(json.dumps(eigenCentrality))
        f.close()

        f = open("output/" + key + "_page_rank_centrality.txt", "w")
        f.write(json.dumps(pageRankCentrality))
        f.close()

        f = open("output/" + key + "_betweenness_centrality.txt",  "w")
        # f.write(json.dumps(betweennessCentrality))
        f.write('Hello world!')
        f.close()

        f = open("output/" + key + "_closeness_centrality.txt", "w")
        f.write(json.dumps(closenessCentrality))
        f.close()

        print('------------------------------------------------\n')

question_b()