class Solution:
	def assignCookies(self, g:list[int], s:list[int]) -> int:
		g.sort()
		s.sort()

		i = j = 0
		while i < len(g):
			while j < len(s) and g[i] > s[j]:
				j += 1
			if j < len(s):
				i += 1
				j += 1
			else:
				break

		return i