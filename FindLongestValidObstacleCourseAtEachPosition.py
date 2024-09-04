class Solution:
	def longestObstacleCourseAtEachPosition(self, nums:list[int]) -> list[int]:
		res = [] # res[i] = height lis ending at i inclusive
		dp = [10**8] * (len(nums) + 1)

		for n in nums:
			index = bisect.bisect(dp, n)
			res.append(index + 1)
			dp[index] = n

		return res