class Solution:
	def numberOfBeams(self, bank:list[str]) -> int:
		prev = bank[0].count("1")
		res = 0

		for i in range(1, len(bank)):
			curr = bank[i].count("1")
			if curr:
				res += (prev * curr)
				prev = curr

		return res