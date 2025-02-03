class Solution:
	def prefixCount(self, words:list[str], pref:str) -> int:

		res = 0
		N = len(pref)

		for w in words:
			if w[:N] == pref:
				res += 1

		return res