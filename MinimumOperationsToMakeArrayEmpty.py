class Solution:
	def minOperations(self, nums:list[int]) -> int:
		count = Counter(nums)
		res = 0

		for n, c in count.items():
			if c == 1:
				return -1
			res += math.ceil(c / 3)

		return res
