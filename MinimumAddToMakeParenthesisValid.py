class Solution:
	def minAddToMakeValid(self, s:str) -> int:
		open_count = 0
		res = 0

		for c in s:
			if c == "(":
				open_count += 1
			else:
				if open_count == 0:
					res += 1
				open_count = max(open_count - 1, 0)

		return res + open_count