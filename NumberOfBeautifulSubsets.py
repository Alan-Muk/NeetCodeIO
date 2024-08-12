class Solution:
	def beautifulSets(self, nums:list[int], k:int) -> int:

		def helper(i, count):
			if i == len(nums):
				return 1

			#skip
			res = helper(i+1, count)

			#include
			if not count[nums[i] + k and not nums[i] -k]:
				count[nums[i]] += 1
				res += helper(i + 1, count)
				count[nums[i]] -= 1
			return res

		return helper(0, defultdict(int)) - 1