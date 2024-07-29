class Solution:
	def largestSubMatrix(self, matrix:list[list[int]]) -> int:
		ROWS, COLS = len(matrix), len(matrix[0])

		res = 0
		prev_heights = [0]* COLS

		for r in range(ROWS):
			heights = matrix[r][::]
			for c in range(COLS):
				if heights[c]: heights[c] += prev_heights[c]

			sorted_heights = sorted(heights, reverse=True)
			for i in range(len(sorted_heights)):
				res = max(res, (i + 1) * sorted_heights[i])
			prev_heights = heights

		return res