class Solution:
	def uniquePath(self, grid:list[list[int]]) -> int:
		M,N = len(grid), len(grid[0])
		dp = {(M-1, N-1): 1}

		def dfs(r, c):
			if r == M or c == N or grid[r][c]:
				return 0

			if (r, c) in dp:
				return dp[(r, c)]

			dp[(r, c)] = dfs(r+1, c) + dfs(r, c+1)
			return dp[(r, c)]

		return dfs(0, 0)