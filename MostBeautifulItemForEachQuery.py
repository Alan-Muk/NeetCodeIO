class Solution:
	def maximumBeauty(self, items:list[list[int]], queries:list[int]) -> list[int]:
		res = []

		for q in queries:
			max_beaut = 0

			for p, b in items:
				if p <= q:
					max_beaut = max(max_beaut, b)

			res.append(max_beaut)


		return res