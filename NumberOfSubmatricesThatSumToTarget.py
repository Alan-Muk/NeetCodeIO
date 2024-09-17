class Solution:
	def numSubmatrixSumTarget(self, matrix:list[list[int]], target:int) -> int:
		ROWS, COLS = len(matrix), len(matrix[0])
		sub_sum = [[0] * COLS for _ in range(ROWS)]

		for r in range(ROWS):
			for c in range(COLS):
				top = sub_sum[r - 1][c] if r > 0 else 0
				left = sub_sum[r][c - 1] if c > 0 else 0
				top_left = sub_sum[r - 1][c - 1] if min(r, c) > 0 else 0

				sub_sum[r][c] = matrix[r][c] + top + left - top_left

		res = 0

		for r1 in range(ROWS):
			for r2 in range(r1, ROWS):
				for c1 in range(COLS):
					for c2 in range(c1, COLS):
						top = sub_sum[r1 - 1][c2] if r1 > 0 else 0
						left = sub_sum[r2][c1 - 1] if c1 > 0 else 0
						top_left = sub_sum[r1 - 1][c1 - 1] if min(r1, c1) > 0 else 0
						cur_sum = sub_sum[r2][c2] - top - left + top_left

						if cur_sum == target:
							res += 1

		return res