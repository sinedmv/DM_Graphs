import networkx as nx
from igraph import *

# IGraph
FileCountries = open("Countries.txt", "r")
G_dist = Graph()
for line in FileCountries:
    data = line.split("\n")
    G_dist.add_vertex(data[0])
FileCountries.close()

FileDist = open("capitalDist.txt", "r")
for line in FileDist:
    data = line.split(" ")
    G_dist.add_edge(data[0], data[1], weight=int(data[2]))
FileDist.close()


print("MST:")
print(G_dist.spanning_tree(G_dist.es["weight"]))
print("-----------------------")

print("Prufer:")
mst = G_dist.spanning_tree(G_dist.es["weight"])
prufer = mst.to_prufer()
for i in prufer:
        print(mst.vs[i]["name"] + "-" + str(i), end=", ")
print()
print("-----------------------")

#Stable Set
print("Stable Set:")
for vertex in G_dist.largest_independent_vertex_sets()[0]:
    print(G_dist.vs[vertex]["name"], end=" ")
print()
print(len(G_dist.largest_independent_vertex_sets()[0]))
print("-----------------------")

# NetworkX

FileCountries = open("Countries.txt", "r")
G = nx.Graph()
for line in FileCountries:
    data = line.split("\n")
    G.add_node(data[0])
FileCountries.close()

FileDist = open("capitalDist.txt", "r")
for line in FileDist:
    data = line.split(" ")
    G.add_edge(data[0], data[1], weight=int(data[2]))
FileDist.close()

print("Radius, Diameter and Center")
print(nx.radius(G))
print(nx.diameter(G))
print(nx.center(G))

# Matching
print("Matching:")
print(nx.max_weight_matching(G))
