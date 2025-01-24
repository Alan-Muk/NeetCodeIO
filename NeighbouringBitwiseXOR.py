class Solution:
	def doesValidArrayExist(self, derived:list[int]) -> bool:
		first = 0
		last = 0

		for n in derived:
			if n:
				last = ~last

		return first == last