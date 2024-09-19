class Solution:
	def minFallingPathSum(self, grid:list[list[int]]) -> int:
		N = len(grid)
		cache = {}

		def helper(r, c):
			if r == N - 1:
				return grid[r][c]
			if (r, c) in cache:
				return cache[(r, c)]

			res = float("inf")
			for next_col in range(N):
				if c != next_col:
					res =min(res, grid[r][c] + helper(r+1, next_col)) 

			cache[(r, c)] = res
			return res

		for c in range(N):
			res = min(res, helper(0,c))

		return res