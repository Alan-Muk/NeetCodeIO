class NumArray:

	def __init__(self, nums:list[int]):
		self. prefix = []
		cur = 0

		for n in nums:
			cur += n
			self.prefix.append(cur)


	def sumRange(self, left:int, right:int) -> int:
		rightSum = self.prefix[right]
		leftSum = self.prefix[left - 1] if left > 0 else 0
		return rightSum - leftSum
