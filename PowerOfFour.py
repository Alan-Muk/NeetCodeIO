class Solution:
	def ispowerOfFour(self, n:int) -> bool:
		if n == 1:
			return True

		if n <= 0 or n % 4:
			return False

		return self.ispowerOfFour(n // 4)