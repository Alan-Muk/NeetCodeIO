class Solution:
	def numberOfSeniorCitizen(self, details:list[str]) -> int:
		res = 0

		for d in details:
			if int(d[11:13]) > 60:
				res += 1

		return res