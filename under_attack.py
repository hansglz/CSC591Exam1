import collections, json, time
import random, copy

import pandas as pd
import numpy as np
import networkx as nx
import networkx.classes.graph as gp
import matplotlib.pyplot as plt
from collections import Counter

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
    # fbGraph = nx.from_pandas_edgelist(facebook, "start_node", "end_node")
    # randomGraph = nx.gnp_random_graph(4000, 0.25)
    # powerlawGraph = nx.powerlaw_cluster_graph(4000, 2, 0.1)
    # print("E-R random graph is connected? " + str(nx.is_connected(randomGraph)))
    # print("Power-Law random graph is connected? " + str(nx.is_connected(powerlawGraph)))

    # degree_sequence = sorted([d for n, d in g.degree()], reverse=True)
    # degreeCount = collections.Counter(degree_sequence)
    # deg, cnt = zip(*degreeCount.items())
    # cs = np.cumsum(cnt)
    randomGraph = generate_er_random_graph()
    powerLawGraph = generate_power_law_graph()

    print('E-R random graph:')
    measure_graph(randomGraph)
    print('\n-------------------------------\n')
    print('Power-Law graph:')
    measure_graph(powerLawGraph)


def generate_er_random_graph():
    n = 1000
    p = 0.01

    return nx.erdos_renyi_graph(n, p)

def generate_power_law_graph():
    # Create a new graph
    # g = nx.Graph()
    #
    # # Add nodes to the graph
    # g.add_nodes_from(range(0, 1001))
    #
    # # Add edges to the graph using a power-law degree distribution
    # for node in g.nodes():
    #     for neighbor in g.nodes():
    #         if node != neighbor:
    #             if random.random() < (1 / abs(node - neighbor)):
    #                 g.add_edge(node, neighbor)

    n = 1000
    m = 10
    exponent = 2.5
    p_triangle = 0.1

    g = nx.powerlaw_cluster_graph(n, m, p=p_triangle)

    return g

def plot_ccdf(g):
    # Plot the degree distribution of the graph
    # plt.hist(sorted(list(nx.degree(g))), bins=100)
    # plt.xlabel('Degree')
    # plt.ylabel('Number of nodes')
    # plt.show()
    # plt.clf()

    # Compute the degree of each node
    degrees = g.degree()
    degree_counts = Counter([d[1] for d in degrees])

    # Compute the CCDF of the degree distribution
    # ccdf = nx.utils.cumulative_distribution(degrees)
    # ccdf = nx.utils.powerlaw_sequence(max(degrees), exponent=2.5)
    ccdf_data = sorted(degree_counts.items(), key=lambda x: x[0], reverse=True)

    # Plot the CCDF on a log-log scale
    deg, cnt = zip(*ccdf_data)
    cs = np.cumsum(cnt)
    plt.loglog(deg, cs, linestyle='none', marker='.')
    plt.xlabel('Degree')
    plt.ylabel('Probability')
    plt.title('CCDF of Node Degrees')
    plt.show()

def measure_graph(g):
    print('Number of nodes inside the graph: {}'.format(g.number_of_nodes()))
    print('Number of edges insidge the graph: {}'.format(g.number_of_edges()))

    g_components_cnt = nx.number_connected_components(g)
    if nx.is_connected(g):
        print('The graph is connected.')
        algebraic_conn = nx.algebraic_connectivity(g)
        print("The graph's algebraic connectivity is {}.".format(algebraic_conn))
        plot_ccdf(g)
        print('Random attack started.')
        gg = copy.deepcopy(g)
        random_attack(gg)
        print('\nOrganized attack started.')
        gg = copy.deepcopy(g)
        organized_attack(gg)
    else:
        print('The graph is not connected, and it has {} connected components'.format(g_components_cnt))

def random_attack(g):
    connectivity = []
    for i in range(100):
        # if i % 2 == 0:
        #     continue
        # delete a random node from the graph
        node = random.choice(list(g.nodes()))
        print('Round: {}, node deleted: {}, it has {} neighbors.'.format(i+1, node, g.degree(node)))
        # g.remove_node(node)
        gp.Graph.remove_node(g, node)

        # judge if the graph is still connected after the removal
        if not nx.is_connected(g):
            print('The graph is no longer connected, currently there are {} components.'
                  .format(nx.number_connected_components(g)))

        # compute the connectivity of the graph
        conn = nx.algebraic_connectivity(g)

        # store the connectivity phases
        connectivity.append(conn)

    # plot the attacking result
    plt.plot(connectivity, label='Algebraic Connectivity')
    plt.xlabel('Iteration')
    plt.legend()
    plt.show()
    print('The connectivity transformation list: {}'.format(connectivity))

def organized_attack(g):
    connectivity = []
    susceptible = []

    # Pick a random node to start the attack
    cur_node = random.choice(list(g.nodes()))

    for i in range(100):
        # Pick a random node from the neighbors of the node that under attack
        neighbors = nx.neighbors(g, cur_node)
        for neighbor in neighbors:
            if neighbor not in susceptible:
                susceptible.append(neighbor)
        next_node = random.choice(susceptible)
        susceptible.remove(next_node)

        # Remove one node per iteration
        print('Round: {}, node deleted: {}, it has {} neighbors.'.format(i+1, cur_node, g.degree(cur_node)))
        # g.remove_node(cur_node)
        gp.Graph.remove_node(g, cur_node)
        cur_node = next_node

        # compute the connectivity of the graph
        conn = nx.algebraic_connectivity(g)

        # store the connectivity phases
        connectivity.append(conn)

    # plot the attacking result
    plt.plot(connectivity, label='Algebraic Connectivity')
    plt.xlabel('Iteration')
    plt.legend()
    plt.show()
    print('The connectivity transformation list: {}'.format(connectivity))

solution()