class Solution:
	def findMatrix(self, nums:list[int]) -> list[list[int]]:
		count = defaultdict(int)
		res = []

		for n in nums:
			row = count[n]
			if len(res) == row:
				res.append([])

			res[row].append(n)
			count[n] += 1


		return res