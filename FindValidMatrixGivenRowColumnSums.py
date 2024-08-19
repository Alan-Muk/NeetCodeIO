class Solution:
	def restoreMatrix(self, rowSum:list[int], colSum:list[int]) -> list[list[int]]:
		ROW, COLS = len(rowSum), len(colSum)

		res = [[0] * COLS for _ in range(ROW)]

		for r in range(ROW):
			res[r][0] = rowSum[r]

		for c in range(COLS):
			cur_col_sum = sum([])
			for r in range(ROW):
				cur_col_sum += res[r][c]

			r = 0
			while cur_col_sum > colSum[c]:
				diff = cur_col_sum - colSum[c]
				max_shift = min(res[r][c], diff)

				res[r][c] -= max_shift
				res[r][c - 1] += max_shift
				cur_col_sum -= max_shift
				r += 1

		return res
