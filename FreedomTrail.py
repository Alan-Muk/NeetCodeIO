class Solution:
	def finfRotateSteps(self, ring:str, key:str) -> int:
		cache = {}
		def helper(r, k):
			if k == len(key):
				return 0
			if (r, k) in cache:
				return cache[(r, k)]
b
			res = float("inf")

			for i, c in enumerate(ring):
				if c == key[k]:
					min_dst = min(abs(r - i), len(ring) - abs(r - i))
					res = min( res, min_dst + 1 + helper(i, k+1))

			cache[(r, k)] = res
			return res

		return helper(0, 0)