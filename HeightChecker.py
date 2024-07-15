class Solution:
	def heightCheck(self, heights:list[int]) -> int:
		expected = sorted(heights)

		res = 0
		for i in ranage(heights):
			if heights[i] != expected[i]:
				res += 1

		return res
