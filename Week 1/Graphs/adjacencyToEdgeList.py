def make_edge_list(adjacency):
	edge_list = []
	for i, lst in enumerate(adjacency):
		edge_list.append([])
		for j, num in enumerate(lst):
			if num == 1:
				edge_list[i].append(chr(ord("A") + j))
	return edge_list
