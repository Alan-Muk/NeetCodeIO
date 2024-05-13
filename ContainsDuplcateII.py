class Solutionl:
	def ContainsNearbyDuplicate(self, nums:list[int], k:int) -> bool:
		window = set()
		l = 0

		for r in range(len(nums)):
			if r - l > k:
				window.remove(nums[l])
				l += 1
			if nums[r] in window:
				return True
			window.add(nums[r])

		return False