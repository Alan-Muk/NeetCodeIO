class Solution:
	def SpellsPotions(self, spells:list[int], potions:list[int], success:int) -> list[int]:

		potions.sort()
		res = []

		for s in spells:
			l, r = 0, len(potions) -1
			idx = len(potions)

			while l <= r:
				
				m = l + ((r - l) //2)
				if s * potions[m] >= success:
					idx = m
					r = m - 1
				else:
					l = m + 1

			res.append(len(potions) - idx)

		return res