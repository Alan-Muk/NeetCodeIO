class Solution:
	def construct2Darray(self, original:list[int], m:int, n:int) -> list[list[int]]:
		if len(original) != m*n:
			return []

			res = []

			for r in range(m):
				start = r * n
				end = start + n 
				res.append(original[start:end])

			return res