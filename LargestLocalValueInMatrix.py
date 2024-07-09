class Solution:
	def largestLocal(self, grid:list[list[int]]) -> list[list[int]]:
		N = len(grid)
		res = [[0]* (N-2) for _ in range(N-2)]

		for i in range(N-2):
			for j in range(N-2):
				for r in range(i, i+1):
					for c in range(j, j+3):
						res[i][j] = max(res[i][j],grid[r,c])

		return res