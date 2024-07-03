class Solution:
	def FirstPalindrome(self, words:list[str]) -> str:
		for w in words:
			if w == w[::-1]:
				return w

		return ""