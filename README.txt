========================
 Christofides Algorithm
========================

This package(Christofides) provides a way to implement Christofides algorithm
for solving Travelling Saleman Problem(TSP) to obtain an approximate solution
on an undirected graph(Distance Matrix) provided as an upper Triangular matrix.
The Distance from a node on to itself is assumed 0.

Usage
======

Use the compute() function which takes as input a distance_matrix and returns a Christofides solution as follows::

	from Christofides import christofides
	TSP = christofides.compute(distance_matrix)

or::

	import Christofides
	TSP = Christofides.christofides.compute(distance_matrix)
	
The Distance Matrix is an upper Triangular matrix with distance from a node on to itself 0, since Christofides algorithm 
could only be applied for undirected graphs. Also the distance between a node on to itself is practically 0.
Example for distance_matrix is as follows,
distance_matrix = ::

	[[0,45,65,15],
	 [0,0,56,12],
	 [0,0,0,89],
	 [0,0,0,0]] 
	 
The above distance_matrix should be provided as an input to christofides.compute(), when we want to calculate TSP for
distance = ::
	
	[[0,45,65,15],
	[45,0,56,12],
	[65,56,0,89],
	[15,12,89,0]]
	
christofides.compute(distance_matrix) returns a Dictionary with following Keys:
	Christofides_Solution,  
	Travel_Cost,
	MST, 
	Odd_Vertices
	Indexes, 
	Multigraph, 
	Euler_Tour
		
* Christofides_Solution: A list consisting of approximate tour for TSP.
	Use: TSP['Chistofides_Solution']
* Travel_Cost: The cost of TSP tour generated.
	Use: TSP['Travel_Cost']
* MST: The minimum spanning tree generated during the Christofides algorithm.
	Use: TSP['MST']
* Odd_Vertices: A list of odd vertices of minimum spanning tree.
	Use: TSP['Odd_Vertices']
* Indexes: List of edges from minimum cost perfect matching of odd vertices.
	Use: TSP['Indexes']
* Multigraph: Edges of multigraph formed after Indexing.
	Use: TSP['Multigraph']
* Euler_Tour: The Euler Tour of the Multigraph.
	Use: TSP['Euler_Tour']
		
Support Functions in christofides
=================================

- _csr_gen_triples(csr_matrix)
- _odd_vertices_of_MST(distance_matrix, number_of_nodes)
- min_Munkres(distance_matrix, bipartitie_graphs)
- Munkres_cost(indexes, bipartite_graph)
- bipartite_Graph(distance_matrix, bipartite_set, odd_vertices)
- create_Multigraph(distance_matrix, MST, indexes, odd_vertices)
- Euler_Tour(multigraph)
- shortcut_Euler_Tour(tour)
- cost(christofides_tour, distance_matrix)
	
Install
=======

python setup.py install
	
Additional Packages
===================

scipy, numpy, networkx, munkres
