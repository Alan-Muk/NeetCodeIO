class Solution:
	def findSmallestSetOfVertices(self, n:int, edges:list[list[int]]) -> list[int]:
		incoming = collections.defaultdict(list)

		for src, dst in edges:
			incoming[dst].append(src)

		res = []
		for i in range(n):
			if not incoming[i]:
				res.append(i)

		return res
