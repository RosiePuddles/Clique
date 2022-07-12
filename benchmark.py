"""
Benchmarking file
"""
from main import NeighbourhoodGroup
from time import time


class Benchmark:
	"""
	Benchmarking class

	Attributes:
		N: Maximum size graph to benchmark
		r: Number of repetitions for each benchmark
	"""
	N = 500
	r = 25

	def __init__(self):
		pass

	def bench(self):
		for f in dir(self):
			if f[:6] == "bench_":
				data = self.__getattribute__(f)()
				r = "x,min,mean,max\n" + "\n".join([",".join([str(i) for i in row]) for row in data])
				with open(f"res/{f[6:]}.csv", "w") as F:
					F.write(r)
				F.close()
			elif f[:7] == "bench2_":
				data = self.__getattribute__(f)()
				r = "x,y,min,mean,max\n" + "\n".join([",".join([str(i) for i in row]) for row in data])
				with open(f"res/{f[7:]}.csv", "w") as F:
					F.write(r)
				F.close()

	def abench2_complete(self) -> [(int, int, float, float, float)]:
		"""
		Benchmark complete graphs for 2<n<N/4 and 2<k<=n
		:return: None
		"""
		data = []
		for n in range(2, int(self.N / 4)):
			full = set(range(n))
			g = dict([(i, full - {i}) for i in range(n)])
			for k in range(2, n + 1):
				print(f"\rComplete: n={str(n).rjust(3)}, k={str(k).rjust(3)}", end="")
				t = []
				for _ in range(self.r):
					start = time()
					NeighbourhoodGroup(g, 2)
					t.append(time() - start)
				data.append((n, k, min(t), sum(t) / len(t), max(t)))
		print()
		return data

	def abench_complete500(self) -> [(int, float, float, float)]:
		"""
		Benchmark a complete graph with 500 nodes
		:return: None
		"""
		data = []
		full = set(range(self.N))
		g = dict([(i, full - {i}) for i in range(self.N)])
		for k in range(5, self.N):
			print(f"\rComplete n=500: k={k}", end="")
			t = []
			for _ in range(self.r):
				start = time()
				NeighbourhoodGroup(g, k)
				t.append(time() - start)
			data.append((k, min(t), sum(t) / len(t), max(t)))
		print()
		return data

	def abench_linear(self) -> [(int, float, float, float)]:
		"""
		Benchmark linear graphs
		:return: None
		"""
		data = []
		for n in range(5, self.N):
			print(f"\rLinear: n={n}", end="")
			t = []
			g = {0: {1}, n - 1: {n - 2}}
			for i in range(1, n - 1):
				g[i] = {i - 1, i + 1}
			for _ in range(self.r):
				start = time()
				NeighbourhoodGroup(g, 2)
				t.append(time() - start)
			data.append((n, min(t), sum(t) / len(t), max(t)))
		print()
		return data

	def abench_cycle(self) -> [(int, float, float, float)]:
		"""
		Benchmark cycle graphs
		:return: None
		"""
		data = []
		for n in range(5, self.N):
			print(f"\rCycle: n={n}", end="")
			t = []
			g = {0: {1, n - 1}, n - 1: {0, n - 2}}
			for i in range(1, n - 1):
				g[i] = {i - 1, i + 1}
			for _ in range(self.r):
				start = time()
				NeighbourhoodGroup(g, 2)
				t.append(time() - start)
			data.append((n, min(t), sum(t) / len(t), max(t)))
		print()
		return data

	def bench2_bipartite(self) -> [(int, int, float, float, float)]:
		data = []
		for n in range(2, int(self.N / 4)):
			for m in range(2, int(self.N / 4)):
				print(f"\rBipartite: {str(n).rjust(3)},{str(m).rjust(3)}", end="")
				left = set(range(n, n + m))
				right = set(range(n))
				t = []
				g = dict([*[(t, left) for t in range(n)], *[(t, right) for t in range(n, n + m)]])
				for _ in range(self.r):
					start = time()
					NeighbourhoodGroup(g, 2)
					t.append(time() - start)
				data.append((n, m, min(t), sum(t) / len(t), max(t)))
		print()
		return data


Benchmark().bench()
