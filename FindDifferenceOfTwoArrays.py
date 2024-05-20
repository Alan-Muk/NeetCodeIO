class Solution:
	def Difference(self, nums1:list[int], nums2:list[int]) -> list[list[int]]:
		nums1Set, nums2Set = set(nums1), set(nums2)
		res1, res2 = set(), set()

		for n in nums1:
			if n not in nums2Set: 
				res1.add(n)
				
		for n in nums2:
			if n not in nums1Set:
				res2.add(n)

		return [list(res1), list(res2)]
