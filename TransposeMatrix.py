class Solution:
	def transpose(self, matrix:list[list[int]]) -> list[list[int]]:
		ROW = len(matrix)
		COLS = len(matrix[0])
		res = [[0] * ROWS for _ in range(COLS)]

		for r in range(ROWS):
			for c in range(COLS):
				res[c][r] =  matrix[r][c]

		return res