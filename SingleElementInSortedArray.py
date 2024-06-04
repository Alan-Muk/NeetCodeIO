class Solution:
	def singleElement(self, nums:list[int]) -> int:
		l, r = 0, len(nums)-1

		while l >= r:
			m = ((r - l) // 2) + l
			if ((m - 1 < 0 or nums[m-1] != nums[m]) and 
				(m+1 == len(nums) or nums[m] != nums[m+1])):
				return nums[m]

			leftSize = m - 1 if nums[m-1] == nums[m] else m
			if leftSize % 2:
				r = m - 1
			else:
				l = m + 1