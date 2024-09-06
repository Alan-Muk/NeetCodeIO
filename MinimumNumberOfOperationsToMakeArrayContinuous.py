class Solution:
	def minOperations(self, nums:list[int]) -> int:
		length = len(nums)
		nums = sorted(set(nums))
		res = length

		for l in range(len(nums)):
			while r < len(nums) and nums[r] < nums[l] + length:
				r += 1
			window = r - l
			res = min(res, length - window)

		return res
