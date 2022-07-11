def NeighbourhoodGroup(graph: {int: {int}}, k: int) -> bool:
	def inner(Q: {int}, I: {int}, t: int) -> bool:
		if t == 1 and len(I) != 0:
			return True
		for n in I:
			if inner(Q.union({n}), I.intersection(graph[n]), t - 1):
				return True
		return False
	if k == 1 and len(graph) != 0:
		return True
	for n in graph:
		if inner({n}, graph[n], k - 1):
			return True
	return False