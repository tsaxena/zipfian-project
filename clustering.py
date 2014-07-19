from collections import defaultdict
import networkx as nx
import numpy
from scipy.cluster import hierarchy
from scipy.spatial import distance
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import seaborn as sns


def trim_degrees(G, degree=1):
    G2 = G.copy()
    d = nx.degree(G)
    for n in G2.nodes():
        if d[n] <= degree: G2.remove_node(n)
    return G2


def create_hr(G):
   """
   Create heirarchical cluster of a graph G from distance matrix
   """
   # create shortest path matrix
   labels=G.nodes()
   path_length = nx.all_pairs_shortest_path_length(G)



def main():
    #read in the graph file
    G = nx.read_edgelist('like.graph', delimiter=',', nodetype=str)
    print "Number of nodes before trimming", len(G.nodes())
    G = trim_degrees(G)
    print "Number of nodes after trimming", len(G.nodes())



if __name__ == '__main__':
    main()