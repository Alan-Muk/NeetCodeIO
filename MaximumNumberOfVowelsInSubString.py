class Solution:
	def maxNumberVowel(self, s:str, k:int) -> int:
		vowelSet = {'a', 'e', 'i', 'o', 'u'}

		count, res, l = 0
		for r in range(len(s)):

			count += 1 if s[r] in vowelSet else 0
			if r - l + 1 > k:
				count -= 1 if s[l] in vowelSet else 0
				l += 1
			res = max(res, count)

		return res