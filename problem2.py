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

def calDis(degree_list, degree_list_final, n):
    res = 0
    for i in range(len(degree_list)):
        res += abs(degree_list[i] - degree_list_final[i])
    return res / n

def solution():
    g = nx.from_pandas_edgelist(facebook, "start_node", "end_node")
    n, e = g.number_of_nodes(), g.number_of_edges()
    degree_list = [d for _, d in g.degree()]
    degree_sum = sum(degree_list)
    degree_list_final = [d / degree_sum for d in degree_list]



solution()