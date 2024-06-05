class Solution:
	def reverseWord(self, s:str) -> str:
		s = list(s)
		l = 0
		for r in range(len(s)):
			if s[r] == " " or r == len(s)-1:
				tempL, tempR = l, r - 1


				if r == len(s)-1:
					tempR = r
				while tempL < tempR:
					s[tempL], s[tempR] = s[tempR], s[tempL]
					tempL += 1
					tempR -= 1

				l = r + 1

		return "".join(s)