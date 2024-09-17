class Solution:
	def kInversePairs(self, n:int, k:int) -> int:
		mod = 10**9 + 7

		cache = {} 

		def count(n, k):
			if n == 0:
				return 1 if k == 0 else 0
			if k < 0:
				return 0
			if (n, k) in cache:
				return cache[(n, k)]

			res = 0
			for i in range(n):
				cache[(n, k)] = (cache[(n, k)] + count(n - 1, k - 1)) % mod
			return cache[(n, k)]

		return count(n, k)
