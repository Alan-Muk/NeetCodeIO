class Solution:
	def minimumScore(self, n:int, roads:list[list[int]]) -> int:
		adj = defaultDict(list) #node:lsit[neighbour, dist]

		for src, dst, dist in roads:
			adj[src].append((dst, dist))
			adj[dst].append((src, dist))

		def dsf(i):
			if i in visit:
				return
			visit.add(i)

			nonlocal res
			for nei, dist in adj[i]:
				res = min(res, dist)
				dfs(nei)


		res = float("inf")
		visit = set()
		dfs(i)
		return res
