class Solution:
	def minimizeXOR(self, nums1:int, nums2:int) -> int:

		def count_bits(n):
			res = 0
			while n > 0:
				res += 1 & n
				n = n >> 1
			return res

		cnt1. cnt2 = count_bits(nums1), count_bits(nums2)

		x = nums1
		i = 0

		# removi
		while cnt1 > cnt2:
			if x & (1 << 1):
				cnt1 -= 1
				x = x ^ (1 << i)

			i += 1
		# add
		while cnt1 < cnt2:
			if x & (1 << 1) == 0:
				cnt1 += 1
				x = x | (1 << i)

			i += 1



		return x