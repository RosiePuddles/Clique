"""
Testing file
"""
import unittest
# from main import NeighbourhoodGroup
from optimised import NeighbourhoodGroup


class Tests(unittest.TestCase):
	"""
	Unit testing class to heuristically test the neighbourhood search algorithm

	Attributes:
		N: Maximum graph size (in terms of nodes) Please note that for larger graphs a recursion depth limit may be
			reached and the test may fail
	"""
	N = 500

	def test_complete(self):
		"""
		Complete graph test
		:return: None
		"""
		for n in range(2, self.N):
			all = set(range(n))
			g = dict([(i, all - {i}) for i in range(n)])
			self.assertTrue(NeighbourhoodGroup(g, n))

	def test_cycle(self):
		"""
		Cycle graph test
		:return: None
		"""
		for n in range(2, self.N):
			g = {0: {1, n - 1}, n - 1: {0, n - 2}}
			for i in range(1, n - 1):
				g[i] = {i - 1, i + 1}
			self.assertTrue(NeighbourhoodGroup(g, 2))

	def test_linear(self):
		"""
		Linear graph test
		:return: None
		"""
		for n in range(2, self.N):
			g = {0: {1}, n - 1: {n - 2}}
			for i in range(1, n - 1):
				g[i] = {i - 1, i + 1}
			self.assertTrue(NeighbourhoodGroup(g, 2))

	def test_bipartite(self):
		"""
		Complete bipartite graph test
		:return: None
		"""
		for n in range(1, self.N):
			for m in range(1, self.N):
				left = set(range(n, n + m))
				right = set(range(n))
				g = dict([*[(t, left) for t in range(n)], *[(t, right) for t in range(n, n + m)]])
				self.assertTrue(NeighbourhoodGroup(g, 2))


if __name__ == '__main__':
	unittest.main()
