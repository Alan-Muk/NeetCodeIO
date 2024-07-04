class Solution:
	def new21Game(self, n:int, k:int, maxPoints:int) -> float:
		# cache = {}

		# def dfs(score):
		# 	if score >= k:
		# 		return 1 if score <= n else 0

		# 	if score in cache:
		# 		return cache[score]

		# 	prob = 0
		# 	for i in range(1, maxPoints + 1):
		# 		prob += dfs(score + i)

		# 	cache[score] = prob / maxPoints
		# 	return cache[score]

		# return dfs(0)
		if k == 0:
			return 1.0

		windowSum = 0
		for i in range(k, k + maxPoints):
			windowSum += 1 if i <= n else 0

		dp = {}
		for i in range(k-1, -1, -1):
			dp[i] = windowSum/maxPoints
			remove = 0
			if i + maxPoints <= n:
				remove = dp.get(i + maxPoints, 1)

			windowSum += dp[i] - remove

		return dp[0]