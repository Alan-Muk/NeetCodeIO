class Solution:
	def minEnd(self, n:int, x:int) -> int:
		res = x

		i_x = 1
		i_n = 1

		while i_n < n - 1:
			if i_x & x == 0:
				if i_n & (n - 1):
					res = res | i_x
				i_n = i_n << 1

			i_x = i_x << 1

		return res

		# for _ in range(n - 1):
		# 	res += 1
		# 	res = res | x

		# return res