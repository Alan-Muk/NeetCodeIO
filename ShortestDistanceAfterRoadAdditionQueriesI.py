class Solution:
	def shortestDistanceAfterQuery(self, n:int, queries:list[list[int]]) -> list[int]:
		adj = [[i + 1] for i in range(n)]

		def shortest_path():
			q = deque()
			q.append((0, 0))

			visit = set()
			visit.add((0, 0))
			while q:
				cur, length = q.popleft()
				if cur == n - 1:
					return length
				for nei in adj[cur]:
					if nei not in visit:
						q.append((nei, length + 1))
						visit.add(nei)

		res = []
		for src, dst in queries:
			adj[src].append(dst)
			res.append(shortest_path())

		return res
