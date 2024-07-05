class Solution:
	def maximumOddBinary(self, s:str) -> str:
		# count = 0 #num of ones

		# for c in s:
		# 	if c == "1":
		# 		count += 1

		# return (count - 1) * "1" + (len(s) - count) * "0" + "1"
		s = [c for c in s]
		left = 0

		for i in range(len(s)):
			if s[i] == "1":
				s[i], s[left] = s[left], s[i]
				left += 1

		s[left-1], s[len(s) -1] = s[len(s) -1], s[left-1] 

		return "".join(s)
