class Solution:
	def maximunXOR(self, nums:list[int], maximumBit:int) -> list[int]:
		xor = 0

		for n in nums:
			xor ^= n

		mask = 2 ** maximumBit - 1
		answer = []
		for n in reversed(nums):
			answer.append(xor ^ mask)
			xor ^= n

		return answer