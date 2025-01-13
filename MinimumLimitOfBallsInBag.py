class solution:
	def minimumSize(self, nums:list[int], maxOperations:int) -> int:

		def can_divide(max_balls):
			ops = 0
			for n in nums:
				ops += ceil(n / max_balls) - 1
				if ops > maxOperations:
					return False

			return True

		
		l, r = 0, max(nums)
		while l < r:
			m = (l + r) // 2

			if can_divide(m):
				r = m
			else:
				l = m + 1

		return l