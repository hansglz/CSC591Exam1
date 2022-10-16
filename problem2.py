import collections, json, time
from random import randrange

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


def calDis(degree_list, degree_list_final):
    res = 0
    for i in range(len(degree_list)):
        res += abs(degree_list[i] - degree_list_final[i])
    return res / len(degree_list)


def calDegreeList(g, cur, degree_list):
    node = randrange(len(degree_list))
    temp = 0
    for adj in list(g.adj[node]):
        temp += cur[adj]
    cur[node] = temp / degree_list[node]


def solution():
    g = nx.from_pandas_edgelist(facebook, "start_node", "end_node")
    n, e = g.number_of_nodes(), g.number_of_edges()
    degree_list = [d for _, d in g.degree()]
    # cur = degree_list
    cur = []
    for i in range(n):
        cur.append(i+1)

    degree_sum = sum(degree_list)
    weighted_avg = np.average(cur, weights=degree_list)

    degree_list_final = []
    for i in range(n):
        degree_list_final.append(weighted_avg)
    # degree_list_final = [d * v / degree_sum for d, v in (degree_list, cur)]

    dist_list = []
    for i in range(5000):
        dis = calDis(cur, degree_list_final)
        print(dis)
        dist_list.append(dis)
        calDegreeList(g, cur, degree_list)

    # print(dist_list)

solution()
