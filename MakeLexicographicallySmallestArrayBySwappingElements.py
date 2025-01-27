class Solution:
	def makeSmallestArray(self, num:list[int], limit:int) -> list[int]:
		groups = [] #list of queue
		num_to_group = {}

		for n in sorted(num):
			if not groups or abs(n - groups[-1][-1]) > limit:
				groups.append(deque())

			groups[-1].append(n)
			num_to_group[n] = len(groups) - 1

		res = []

		for n in num:
			j = num_to_group[n]
			res.append(groups[j].popleft())

		return res