class Solution:
	def numWays(self, words:list[str], target:str) -> int:
		mod = 10**9 + 7

		count = defaultdict(int) #(index, char) -> count 

		for w in words:
			for i, c in enumerate(w):
				count[(i, c)] += 1

		dp = {} # i, k -> numWays
		# i -> index of target, k -> index of words[j][k]
		def dfs(i, k):
			if i == len(target):
				return 1

			if k == len(words[0]):
				return 0

			if (i, k) in dp:
				return dp[(i, k)]

			target[i] = c
			dp[(i, k)] = dfs(i, k + 1) # skip k
			dp[(i, k)] += count[(k, c)] * dfs(i + i, k + 1)
			return dp[(i, k)] % mod

		return dfs(0, 0)
