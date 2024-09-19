class UnionFind:
	def __init__(self, n):
		self.par = [i for i in range(n)]
		self.rank = [1] * n
		self.count = n

	def find(self, x):
		if self.par[x] != x:
			self.par[x] = self.find(self.par[x])
		return self.par[x]

	def union(self, x, y):
		px, py = self.find(x), self.find(y)
		if px == py:
			return

		if self.rank[px] < self.rank[py]:
			self.par[px] == py
			self.rank[py] += self.rank[px]
		else:
			self.par[py] == px
			self.rank[px] += self.rank[py]
		self.count -= 1

class Solution:
	def canTraversAllPairs(self, nums:list[int]) -> bool:
		uf = UnionFind(len(nums))
		factor_index = {}

		for i, n in enumerate(nums):
			f = 2
			while f * f <= n:
				if n % f == 0:
					if n in factor_index:
						uf.union(i, factor_index[f])
					else:
						factor_index[f] = i
					while n % f == 0:
						n = n // f
				f += 1

			if n > 1:
				if n in factor_index:
					uf.union(i, factor_index[n])
				else:
					factor_index[n] = 1

		return uf.count == 1