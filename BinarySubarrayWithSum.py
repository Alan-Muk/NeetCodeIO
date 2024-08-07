class Solution:
	def subArrayWithSum(self, nums:list[int], goal:int) -> int:
		#subarray where sum < x
		def helper(x):
			if x < 0: return 0

			res = 0
			l, cur = 0, 0
			for r in range(len(nums)):
				cur += nums[r]

				while cur > x:
					cur -= nums[l]
					l += 1
				res += (r - l + 1)

			return res

		return helper(goal) - helper(goal - 1)