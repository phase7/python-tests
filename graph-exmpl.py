graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
             
def fpath(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return path

	if not graph.has_key(start):
		return None
	for node in graph(start):
		if node not in path:
			newpath = fpath(graph, start, end, path)
