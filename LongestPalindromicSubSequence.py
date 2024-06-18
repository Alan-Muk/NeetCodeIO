class Solution:
	def longestPalindromicSubSequence(self, s:str) -> int:
		cache = {}

		def dfs(i, j):
			if i < 0 or j == len(s):
				return 0

			if (i, j) in cache:
				return cache[(i, j)]

			if s[i] == s[j]:
				length = 1 if i == j else 2
				cache[(i, j)] = length + dfs(i - 1, j + 1)

			else:
				cache[(i, j)] = max(dfs(i - 1, j), dfs(i, j + 1))

			return cache[(i, j)]

		for i in range(len(s)):
			dfs(i, i) #odd
			dfs(i, i + 1) # even

		return max(cache.values())