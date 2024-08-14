class Solution:
	def subArrayDivByK(self, nums:list[int], k:int) -> int:
		prefix_sum = 0
		res = 0

		prefix_count = defaultdict(int)
		prefix_count[0] = 1

		for n in nums:
			prefix_sum += n
			remain = prefix_sum % k

			if remain in prefix_count:
				res += prefix_count[remain]
			prefix_count[remain] += 1


		return res