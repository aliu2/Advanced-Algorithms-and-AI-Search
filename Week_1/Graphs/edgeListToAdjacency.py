def make_adjacency_matrix(edge_list):
	adjacency_matrix = []
	for i, lst in enumerate(edge_list):
		adjacency_matrix.append([])
		j = 0
		while j < len(edge_list):
			if chr(ord("A") + j) in lst:
				adjacency_matrix[i].append(1)
			else:
				adjacency_matrix[i].append(0)
			j+=1
	return adjacency_matrix
