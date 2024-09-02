class Solution:
	def largestPathValue(self, colors:str, edges:list[list[int]]) -> int:
		
		adj = defaultdict(list)
		for src, dst in edges:
			adj[src].append(dst)

		def dfs(node):
			if node in path:
				return float("inf")
			if node in visit:
				return 0

			visit.add(node)
			path.add(node)


			color_index = ord(colors[node]) - ord('a')
			count[node][color_index] = 1

			for nei in adj[node]:
				if dfs(nei) == float("inf"):
					return float("inf")
				for c in range(26):
					count[node][c] =  max(count[node][c], (1 if c  == color_index else 0) + count[nei][c])

			path.remove(node)
			return max(count[node])

		n, res = len(colors), 0
		visit, path = set(), set()
		count = [[0] * 26 for i in range(n)] #map count[node][color] -> max freq color]

		for i in range(n) :
			res = max(res, dfs(i))

		return -1 if res == float("inf") else res