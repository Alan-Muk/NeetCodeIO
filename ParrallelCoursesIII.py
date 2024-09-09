class Solution:
	def minimumTime(self, n:int, relations: list[list[int]], time:list[int]) -> int:
		
		adj = defaultdict(list)
		for src, dst in relations:
			adj[src].append(dst)

		max_time = {} 
		def dfs(src):
			if src in max_time:
				return max_time[src]

			res = time[src - 1]
			for nei in adj[src]:
				res = max (res, time[src - 1] +  dfs(nei))
			max_time[src] = res

			return res

		for i in range(1, n+1):
			dfs(i)

		return max(max_time.values())
