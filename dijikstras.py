from collections import deque

def dijikstras(graph, a, b):
    # initialize distances
    dist = {}
    for v in graph:
        dist[v] = float("inf")

'''
function Dijkstra(Graph, source):
2:	for each vertex v in Graph:	// Initialization
3:	dist[v] := infinity	// initial distance from source to vertex v is set to infinite
4:	previous[v] := undefined	// Previous node in optimal path from source
5:	dist[source] := 0	// Distance from source to source
6:	Q := the set of all nodes in Graph	// all nodes in the graph are unoptimized - thus are in Q
7:	while Q is not empty:	// main loop
8:	u := node in Q with smallest dist[ ]
9:	remove u from Q
10:	for each neighbor v of u:	// where v has not yet been removed from Q.
11:	alt := dist[u] + dist_between(u, v)
12:	if alt < dist[v]	// Relax (u,v)
13:	dist[v] := alt
14:	previous[v] := u
15:	return previous[ ]
'''