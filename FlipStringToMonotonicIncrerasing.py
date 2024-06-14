class Solution:
	def minFlipsMonoIncr(self, s:str) -> int:
		res = 0
		count1 = 0

		for c in s:
			if c =="1":
				count1 += 1
			else:
				res = min(res+1, count1)

		return res