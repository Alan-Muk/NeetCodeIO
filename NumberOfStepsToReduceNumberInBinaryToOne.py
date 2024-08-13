class Solution:
	def numSteps(self, s:str) -> int:
		res = 0
		carry = 0

		for i in reverse(range(1, len(s))):
			digit = int(s[i] + carry) % 2
			if digit == 0:
				res += 1
			elif digit == 1: 
				carry = 1
				res += 2

		return res + carry