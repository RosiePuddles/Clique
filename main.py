def NeighbourhoodGroup(graph: {int: {int}}) -> int:
	k = 0
	for n1 in graph:
		if len(graph[n1]) == 0:
			k = max(k, 1)
		elif len(graph[n1]) >= k:
			for n2 in graph[n1]:
				I = graph[n1].intersection(graph[n2])
				t = 0
				while len(I) != 0 and t < 10:
					n3 = list(I)[0]
					k = max(k, len(I.intersection(graph[n3])) + 3)
					I -= graph[n3].union({n3})
					t += 1
	return k
