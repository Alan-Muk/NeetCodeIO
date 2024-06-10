class Solution:
	def totalMoney(self, n:int) -> int:
		day = 0
		deposit = 1
		res = 0

		while day < n:
			res += deposit
			deposit += 1
			day += 1

			if day % 7 == 0:
				deposit = 1 + day // 7

		return res