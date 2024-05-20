class Solution:
	def diagonalSum(self, matrix:list[list[int]]) -> int:
		res, n = 0, len(matrix)

		for i in range(n):
			res += matrix[i][i]
			res += matrix[i][len(matrix) -1 -i]


		return res - (mat[n //2][n // 2] if n % 2 else 0)