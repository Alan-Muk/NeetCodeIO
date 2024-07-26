class Solution:
	def maxElementAfter(self, arr:list[int]) -> int:
		arr.sort()
		prev = float("inf")

		for n in arr:
			prev = min(prev + 1, n)

		return prev