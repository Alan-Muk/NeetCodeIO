class Solution:
	def maxScoreGoodSubArray(self, nums:list[int], k:int) -> int:
		l = r = k
		res = nums[k]
		cur_min = nums[k]

		while l > 0 or r < len(nums) -1:
			left = nums[l - 1] if l > 0 else 0
			right = nums[r + 1] if r < len(nums) - 1 else 0
			if left > right:
				l -= 1
				cur_min = min(cur_min, left)
			else:
				r += 1
				cur_min = min(cur_min, right)

			res = max(res, cur_min * (r - l + 1))

		return res