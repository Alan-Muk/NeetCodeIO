class Solution:
	def maximumBeauty(self, items:list[list[int]], queries:list[int]) -> list[int]:
		items.sort() #[p,b]
		queries = [(q, i) for i, q in enumerate(queries)]
		queries.sort()

		res = [0] * len(queries)
		max_beaut = 0
		j = 0
		for q, i in queries:
			while j < len(items) and items[j][0] <= q:
				max_beaut = max(max_beaut, items[j][1])
				j += 1


			res[i] = max_beaut

		return res	



		# res = []

		# for q in queries:
		# 	max_beaut = 0

		# 	for p, b in items:
		# 		if p <= q:
		# 			max_beaut = max(max_beaut, b)

		# 	res.append(max_beaut)


		# return res