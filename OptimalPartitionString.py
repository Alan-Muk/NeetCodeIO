class Solution:
	def optimalPart(self, s:str) -> int:
		curStr = set()
		res = 1

		for c in s:
			if c in curStr:
				res += 1
				curStr = set()
				curStr.add(c)
			else:
				curStr.add(c)
		return res
