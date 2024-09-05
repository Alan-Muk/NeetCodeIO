class UnionFind:
	def __init__(self, n):
		self.par = [i for i in range(n)]
		self.rank = [1] * n

	def find(self, v1):
		while v1 != self.par[v1]:
			self.par[v1] = self.par[self.par[v1]]
			v1 = self.par[v1]
		return v1

	def union(self, v1, v2):
		p1, p2 = find(v1), find(v2)

		if p1 == p2:
			return False

		if self.rank[p1] > self.rank[p2]:
			self.par[p2] = p1
			self.rank[p1] += self.rank[p2]
		else:
			self.par[p1] = p2
			self.rank[p2] += self.rank[p1]
		return True


class Solution:
	def findCriticalAndPsudoCriticalEdges(self, n:int, edges:list[list[int]]) -> list[list[int]]:

		for i, e in enumerate(edges):
			e.append(i) #[v1, v3, weight, original_index]
		edges.sort(key=lambda e: e[2])

		mst_weight = 0
		uf = UnionFind(n)

		for v1, v2, w, i in edges:
			if uf.union(v1, v2):
				mst_weight += w

		critical, pseudo = [], []

		for n1, n2, e_weight, i in edges:
			#try without curr edge
			weight = 0
			uf = UnionFind(n)

			for v1, v2, w, j in edges:
				if i != j and uf.union(v1, v2):
					weight += w

			if max(uf.rank) != n or weight > mst_weight:
				critical.append(i)
				continue

			#with curr edge
			uf = UnionFind(n)
			uf.union(n1, n2)
			weight = e_weight

			for v1, v2, w, j in edges:
				if uf.union(v1, v2):
					weight += w

			if weight == mst_weight:
				pseudo.append(i)

		return [critical, pseudo]