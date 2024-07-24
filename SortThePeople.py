class Solution:
	def sortPeople(self, names:list[str], heights:list[int]) -> list[str]:

		height_name = {}
		for h, n in zip(heights, names):
			height_name[h] = n

		res = []

		for h in reversed(sorted(heights)):
			res.append(height_name[h])

		return res