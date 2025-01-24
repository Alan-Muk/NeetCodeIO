class Solution:
	def gridGame(self, grid:list[list[int]]) -> int: 
		N = len(grid[0])
		prevRow1, prevRow2 = grid[0].copy(), grid[0].copy()

		for i in range(1, N):
			prevRow1[i] += prevRow1[i - 1]
			prevRow2[i] += prevRow2[i - 1]

		res = float("inf")
		for i in range(N):
			top = prevRow1[-1] - prevRow1[i]
			bottom = prevRow2[i - 1] if i > 0 else 0
			secondRobot = max(top, bottom)
			res = min(res, secondRobot)

		return res