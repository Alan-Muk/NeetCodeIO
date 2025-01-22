class Solution:
	def minCostTicket(self, days:list[int], cost:list[int]) -> int:
		dp = {}

		def dfs(i):
			if i == len(days):
				return 0
			if i in dp:
				return dp[i]

			dp[i] = float("inf")
			j = i
			for cst, dur in zip(cost, [1, 7, 30]):
				
				while j < len(days) and days[j] < days[i] + dur:
					j += 1

				dp[i] = min(dp[i], cost + dfs(j))


			return dp[i]

		return dfs(0)