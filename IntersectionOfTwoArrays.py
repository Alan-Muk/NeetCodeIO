class Solution:
	def intersection(self, nums1:list[int], nums2:list[int]) -> list[int]:
		seen = set(nums1)

		res = []

		for n in nums2:
			if n in seen:
				res.append(n)
				seen.remove(n)

		return res
