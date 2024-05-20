class Solution:
	def signOfArray(self, nums:list[int]) -> int:
		neg = 0

		for n in mums:
			if n == 0:
				return 0
				neg += (1 if n < 0 else 0 )
			
		return -1 if neg % 2 else 1