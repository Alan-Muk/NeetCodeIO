class Solution:
	def minimizeMaximum(self, nums:list[int]) -> int:
		res = nums[0]
		total = nums[0]

		for i in range(1, len(nums)):
			total += nums[i]
			res = max(res, math.ceil(total / (i + 1)))

		return res
