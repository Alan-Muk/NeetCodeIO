class Solution:
	def longestIdealString(self, s:str, k:int) -> int:
		cache = {}
		
		def dfs(i, prev):
			if i == len(s):
				return 0

			if (i, prev) in cache:
				return cache[(i, prev)]

			#skip s[i]
			res = dfs(i+1, prev)

			#include s[i]
			if prev == "" or abs(ord(s[i]) - ord(prev)) <= k:
				res = max(res, 1 + dfs(i+1, s[i]))

			cache[(i, prev)] = res
			return res

		return dfs(0, "")