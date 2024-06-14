class Solution:
	def maxSubarraySumCircular(self, nums:list[int]) -> int:
		globMax, globMin = nums[0], nums[0]
		curMax, curMin = 0, 0
		total = 0

		for n in nums:
			curMax = max(curMax + n, n)
			curMin = min(curMax + n, n)
			total += n
			globMax = max(globMax, curMax)
			globMin = min(globMin, curMin)

		return max(globMax, total - globMin) if globMax > 0 else globMax