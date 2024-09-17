class Solution:
	def numberOfArithmeticSlices(self, nums:list[int]) -> int:
		res, n = 0, len(nums)

		dp = [defaultdict(int) for _ in range(n)] # dp[i][diff]

		for i in range(n):
			for j in range(i):
				diff = nums[i] - nums[j]
				dp[i][diff] += 1 + dp[j][diff]
			res += dp[i][diff] 

		return res - (n * (n - 1) // 2)