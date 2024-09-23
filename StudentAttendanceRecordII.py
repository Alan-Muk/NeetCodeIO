class Solution:
	def checkRecord(self, n:int) -> int:
		mod = 10**9 + 7
		cache = {}
		def count(n):
			if n == 1:
				#(A, L)
				return {(0, 0): 1, (0, 1): 1, (0, 2): 0,
						(1, 0): 1, (1, 1): 0, (1, 2): 0}

			if n in cache:
				return cache[n]

			tmp = count(n - 1)
			res = defaultdict(int)

			#choose p
			res[(0, 0)] = (tmp[(0, 0)] + tmp[(0, 1)] + tmp[(0, 2)])
			res[(1, 0)] = (tmp[(1, 0)] + tmp[(1, 1)] + tmp[(1, 2)])
			#choose L
			res[(0, 1)] = tmp[(0, 0)]
			res[(1, 1)] = tmp[(1, 0)]
			res[(0, 2)] = tmp[(0, 1)]
			res[(1, 2)] = tmp[(1, 1)]
			#choose A
			res[(1, 0)] += (tmp[(0, 0)] + tmp[(0, 1)] + tmp[(0, 2)])
			cache[n] = res
			return res 
		return sum(count(n).values()) % mod