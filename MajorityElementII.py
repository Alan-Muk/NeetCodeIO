class Solution:
	def majorityElement(self, nums:list[int]) -> list[int]:
		count = defaultdict(int)

		for n in nums:
			count[n] += 1

			if len(count) <= 2:
				continue

			new_count = defaultdict(int)
			for n, c in count.items():
				if c > 1:
					new_count[n] = c - 1
			count = new_count


		res = []
		for n in count:
			if nums.count(n) > len(nums) // 3:
				res.append(n)

		return res