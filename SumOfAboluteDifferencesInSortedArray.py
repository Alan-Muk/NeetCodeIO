class Solution:
	def getSumAbsoluteDifference(self, nums:list[int]) -> list[int]:
		total_sum = sum(nums)
		left_sum = 0
		res = []

		for i, n in enumerate(nums):
			right_sum = total_sum - n - left_sum
			left_size, right_size = i, len(nums) - i - 1
			res.append(
				left_size * n - left_sum + 
				right_sum - right_size*n
				)
			
			left_sum += n

		return res