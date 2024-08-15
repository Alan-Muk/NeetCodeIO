class Solution:
	def maxTotalImportance(self, n:int, roads:list[list[int]]) -> int:
		edge_count = [0] * n

		for n1, n2 in roads:
			edge_count[n1] += 1
			edge_count[n2] += 1

		label = 1
		res = 0
		for count in sorted(edge_count):
			res += count * label
			label += 1

		return res