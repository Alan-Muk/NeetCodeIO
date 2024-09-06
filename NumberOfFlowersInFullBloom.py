class Solution:
	def fullBloom(self, flowers:list[list[int]], people:list[int]) -> list[int]:
		
		people = [(p, i) for i, p in enumerate(people)]
		res = [0] * len(people)
		count = 0

		start = [f[0] for f in flowers]
		end = [f[i] for f in flowers]
		heapq.heapify(start)
		heapq.heapify(end)

		for p, i in sorted(people):
			while start and start[0] <= p:
				heapq.heappop(start)
				count += count
			while end and end[0] < p:
				heapq.heappop(end)
				count -= 1
			res[i] = count

		return res