#!/usr/bin/env python

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import numpy as np
from munkres import Munkres
import networkx as nx
import copy
import itertools
from operator import itemgetter
import graph

def _csr_gen_triples(A):
	"""Converts a SciPy sparse matrix in **Compressed Sparse Row** format to
    an iterable of weighted edge triples.

	"""
	graph = nx.Graph()
	nrows = A.shape[0]
	data, indices, indptr = A.data, A.indices, A.indptr
	for i in range(nrows):
		for j in range(indptr[i], indptr[i+1]):
			graph.add_edge(i,indices[j], weight = data[j])   
	return graph.edges(data = 'weight')

def _odd_vertices_of_MST(M, number_of_nodes):
	"""Returns the vertices having Odd degree in the Minimum Spanning Tree(MST).

	"""
	odd_vertices = [0 for i in range(number_of_nodes)]
	for u,v,d in M:
		odd_vertices[u] = odd_vertices[u] + 1
		odd_vertices[v] = odd_vertices[v] + 1
	odd_vertices = [vertex for vertex, degree in enumerate(odd_vertices) if degree % 2 == 1]
	return odd_vertices

def min_Munkres(M, bipartite_graphs):
	"""Implements the Hungarian problem or the Assignment problem to
	find Minimum Cost Perfect Matching(MCPM).

	"""
	m = Munkres()
	minimum = np.inf
	for index,bipartite_graph in enumerate(bipartite_graphs[0]):
		Munkres_indexes = m.compute(bipartite_graph)
		cost = Munkres_cost(Munkres_indexes, bipartite_graph)
		if cost < minimum:
			minimum = cost
			min_index = index
			min_Munkres_indexes = Munkres_indexes
	Munkres_indexes = [[] for i in range(len(min_Munkres_indexes))]
	for index,vertex_set in enumerate(min_Munkres_indexes):
		Munkres_indexes[index].append(bipartite_graphs[1][min_index][0][vertex_set[0]])
		Munkres_indexes[index].append(bipartite_graphs[1][min_index][1][vertex_set[1]])
	return Munkres_indexes

def Munkres_cost(indexes, bipartite_graph):
	"""Returns cost of the edges in Munkres_indexes

	"""
	cost = 0
	for index in indexes:
		cost = cost + bipartite_graph[index[0]][index[1]]
	return cost

def bipartite_Graph(M, bipartite_set, odd_vertices):
	"""
	"""
	bipartite_graphs = []
	vertex_sets = []
	for vertex_set1 in bipartite_set:
		vertex_set1 = list(sorted(vertex_set1))
		vertex_set2 = []
		for vertex in odd_vertices:
			if vertex not in vertex_set1:
				vertex_set2.append(vertex)
		matrix = [[np.inf for j in range(len(vertex_set2))] for i in range(len(vertex_set1))]
		for i in range(len(vertex_set1)):
			for j in range(len(vertex_set2)):
				if vertex_set1[i] < vertex_set2[j]:
					matrix[i][j] = M[vertex_set1[i]][vertex_set2[j]]
				else:
					matrix[i][j] = M[vertex_set2[j]][vertex_set1[i]]
		bipartite_graphs.append(matrix)
		vertex_sets.append([vertex_set1,vertex_set2])
	return [bipartite_graphs, vertex_sets]

def create_Multigraph(M, MST, indexes, odd_vertices):
	"""Creates a MultiGraph consisting of vertices of both
	MST and MCPM.

	"""
	multigraph = nx.MultiGraph()
	for u,v,d in MST:
		multigraph.add_edge(u,v,weight=d)
	for pair in indexes:
		multigraph.add_edge(pair[0],pair[1],weight=M[pair[0]][pair[1]])
	return multigraph
	
def Euler_Tour(multigraph):
	""" Uses Fleury's algorithm to find the Euler Tour of the MultiGraph.

	"""
	tour = []
	temp_graph = nx.MultiGraph()
	graph_nodes = nx.nodes(multigraph)
	current_node = graph_nodes[0]
	tour.append(current_node)
	while nx.number_of_edges(multigraph) > 0: 	
		for edge in multigraph.edges(current_node):
			temp_graph = copy.deepcopy(multigraph)
			temp_graph.remove_edge(edge[0], edge[1], key=None)
			if nx.is_connected(temp_graph):
				tour.append(edge[1])
				current_node = edge[1]
				multigraph.remove_edge(edge[0], edge[1], key=None)
				break
		else:
			tour.append(edge[1])
			current_node = edge[1]
			multigraph.remove_edge(edge[0], edge[1], key=None)
			multigraph.remove_nodes_from(nx.isolates(multigraph))
	return tour

def shortcut_Euler_Tour(tour):
	"""Find's the shortcut of the Euler Tour to obtain the Approximation.

	"""
	Tour = []
	for vertex in tour:
		if vertex not in Tour:
			Tour.append(vertex)
	Tour.append(tour[0])
	return Tour

def cost(christofides_tour, M):
	"""Returns Cost of Tour.

	"""
	Travel_Cost = 0
	christofides_tour = christofides_tour[0:len(christofides_tour)-1]
	previous_vertex = christofides_tour[len(christofides_tour)-1]
	for current_vertex in christofides_tour:
		if previous_vertex > current_vertex:
			Travel_Cost = Travel_Cost + M[current_vertex][previous_vertex]
		else:
			Travel_Cost = Travel_Cost + M[previous_vertex][current_vertex]
		previous_vertex = current_vertex
	return Travel_Cost

def compute(M):
	"""Returns an Approximation for TSP using Christofide's algorithm by
	directing several functions.

	"""
	MST = _csr_gen_triples(minimum_spanning_tree(csr_matrix(M)))
	odd_vertices = _odd_vertices_of_MST(MST, csr_matrix(M).shape[0])
	bipartite_set = [set(i) for i in itertools.combinations(set(odd_vertices), len(odd_vertices)/2)]
	bipartite_graphs = bipartite_Graph(M, bipartite_set, odd_vertices)
	indexes = min_Munkres(M, bipartite_graphs)
	multigraph = create_Multigraph(M, MST, indexes, odd_vertices)
	multiGraph = copy.deepcopy(multigraph)
	euler_tour = Euler_Tour(multigraph)
	Christofides_Solution = shortcut_Euler_Tour(euler_tour)
	Travel_Cost = cost(Christofides_Solution, M)
	return {
			'Christofides_Solution': Christofides_Solution, 
			'Travel_Cost': Travel_Cost, 
			'MST': MST, 
			'Odd_Vertices': odd_vertices, 
			'Indexes': indexes, 
			'Multigraph': multiGraph.edges(data='weight'), 
			'Euler_Tour': euler_tour
			}

if __name__ == "__main__":
	distance_matrix = graph.distance_matrix
	Approximation =  compute(distance_matrix)
	print '\n1.5 Approximation of TSP (Christofide\'s algorithm):', Approximation['Christofides_Solution']
	print 'Travel Cost:', Approximation['Travel_Cost']
	print ''
