class Solution:
	def numWays(self, steps:int, arrLen:int) -> int:
		mod = 10**9 + 7
		dp = {}

		def dfs(i, steps):
			if steps == 0:
				return i == 0
			if (i, steps) in dp:
				return dp[(i, steps)]

			res = dfs(i, steps - 1)

			if i > 0:
				res = (res + dfs(i - 1, steps - 1)) % mod

			if i < arrLen - 1:
				res = (res + dfs(i + 1, steps - 1)) % mod

			dp[(i, steps)] = res

			return res
		
		return dfs(0, steps)