class Solution:
	def search(self, nums:list[int], target:int) -> bool:
		l, r = 0, len(nums) -1

		while l <= r:
			m = l + (r - l) // 2
			if nums[m] == target: return True

			if nums[l] < nums[m]: #left
				if nums[l] <= target < nums[m]:
					r = m -1
				else:
					l = m + 1
			elif nums[l] > nums[m]: #right
				if nums[m] < target <= nums[r]:
					l = m + 1
				else:
					r = m -1
			else:
				l += 1

		return False