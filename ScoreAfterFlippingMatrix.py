class Solution:
	def matrixScore(self, grid:list[list[int]]) -> int:
		ROWS, COLS = len(grid), len(grid[0])

		for r in range(ROWS):
			if grid[r][0] == 0:
				for c in range(COLS):
					grid[r][c] = 0 if grid[r][c] else 1

		for c in range(COLS):
			one_cnt = 0
			for r in range(ROWS):
				one_cnt += grid[r][c]
			if one_cnt < ROWS - one_cnt:
				for r in range(ROWS):
					grid[r][c] = 0 if grid[r][c] else 1

		res = 0
		for r in range(ROWS):
			for c in range(COLS):
				res += grid[r][c] << (COLS - c - 1)

		return res