class Solution:
	def findOddInteger(self, low:int, high:int) -> int:
		length = hihg - low + 1
		count = length // 2
		
		if length % 2 and low % 2:
			count += 1

		return count
