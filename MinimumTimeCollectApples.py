class Solution:
	def maximumTime(self, n:int, edges:list[list[int]], hasApple:list[bool]) -> int:
		adj = collections.defaultdict(list)

		for par, child in edges:
			adj[par].append(child)
			adj[child].append(par)


		def dfs(cur, par):
			time = 0

			for child in adj[cur]:
				if child == paar:
					continue

				childTime = dfs(child, cur)
				if childTime or hasApple[child]:
					time += 2 + childTime

			return time

		return dfs(0, -1)