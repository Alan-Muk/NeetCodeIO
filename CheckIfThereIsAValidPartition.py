class Solution:
	def validPartition(self, nums:list[int]) -> bool:
		dp = {}

		def dfs(i):
			if i == len(nums):
				return True

			if i in dp:
				return dp[i]

			res = False
			if i < len(nums) -1 and nums[i] == nums[i + 1]:
				res =  dfs(i + 2)

			if i < len(nums) -2:
				if (nums[i] == nums[i + 1] == nums[i + 2] or 
			  		nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1):
					res = res or dfs(i + 3)

			dp[i] = res

			return res

		return dfs(0)