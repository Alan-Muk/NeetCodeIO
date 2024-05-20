class Solution:
	def findMaxForm(self, strs:list[str], m:int, n:int) -> int:

		dp = {}

		def dfs(i, m, n):
			if i == len(strs):
				return 0
			if (i, m, n) in dp:
				return dp[(i, m, n)]

			mCount, nCount = strs[i].count("0"), strs.count("1")
			dp[(i, m, n)] =  dfs(i+1, m, n)
			if mCount <= m and nCount <= n:
				dp[(i, m, n)] = max (dfs(i, m, n), 1 + dfs(i+1, m-mCount, n-nCount))

			return dp[(i, m, n)]

		return dfs(0, m, n)