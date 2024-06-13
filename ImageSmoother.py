class Solution:
	def imageSmoother(self, img:list[list[int]]) -> list[list[int]]:
		ROWS = len(img)
		COLS = len(img[0])

		res = [[0] * COLS for _ in range(ROWS)]

		for r in range(ROWS):
			for c in range(COLS):
				total, count = 0, 0
				for i in range(r-1, r+2):
					for j in range(c-1, c+2):
						if i < 0 or i == ROWS or j < 0 or j == COLS:
							continue
						total += img[i][j]
						count += 1

				res[r][c] = total // count


		return res