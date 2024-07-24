class Solution:
	def sortArrayByFreq(self, nums:list[int]) -> list[int]:
		count = Counter(nums)

		def custom_sort(n):
			return(count[n], -n)

		nums.sort(key = custom_sort)

		return nums