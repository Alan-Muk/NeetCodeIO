class Solution:
	def countUnguarded(self, n:int, m:int, guards:list[list[int]], walls:list[list[int]]) -> int:
		grid = [[0] * n for _ in range(m)]

		for r, c in guards:
			grid[r][c] = 1

		for r, c in walls:
			grid[r][c] = 2

		def mark_guarded(r, c):
			for row in range(r + 1, m):
				if grid[row][c] in [1, 2]:
					break
				grid[row][c] = 3

			for row in reversed(range(0, r)):
				if grid[row][c] in [1, 2]:
					break
				grid[row][c] = 3

			for col in range(c + 1, n):
				if grid[r][col] in [1, 2]:
					break
				grid[r][col] = 3

			for col in reversed(range(0, c)):
				if grid[r][col] in [1, 2]:
					break
				grid[r][col] = 3

		for r, c in guards:
			mark_guarded(r, c)

		res = 0
		for row in grid:
			for n in row:
				if n == 0:
					res += 1

		return res
