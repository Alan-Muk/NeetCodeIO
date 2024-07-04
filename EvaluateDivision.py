class Solution:
	def calcEquation(self, equations:list[list[str]], values:list[float], queries:list[list[str]]) -> list[float]:
		adj = collectons.defaultdict(list) # map a -> [b, a/b]
		for i, eq in enumerate(equations):
			a, b = eq
			adj[a].append([b, values[i]])
			adj[b].append([a, 1/values[i]])

		def bfs(src, target):
			if src not in adj or target not in adj:
				return -1

			q, visit = deque(), set()
			q.append([src, 1])
			visit.add(src)

			while q:
				n, w = q.popleft()
				if n == target:
					return w
				for nei, weight in adj[n]:
					if nei not in visit:
						q.append([nei, w * weight])
						visit.add(nei)
			return -1

		return [bfs(q[0], q[i]) for q in queries]

