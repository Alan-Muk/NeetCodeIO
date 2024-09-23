class Solution:
	def maxScoreWord(self, words:list[str], letters:list[str], score:list[int]) -> int:
		letter_count = Counter(letters)

		def can_form_word(w, letter_count):
			word_count = Counter(w)

			for c in word_count:
				if word_count[c] > letter_count[c]:
					return False
			return True

		def get_score(w):
			res = 0
			for c in w:
				res += score[ord(c) - ord('a')]
			return res

		def backtrack(i):
			if i == len(words):
				return 0

			#skip
			res = backtrack(i + 1)
			#include
			if can_form_word(words[i], letter_count):
				for c in words[i]:
					letter_count[c] -= 1
				res = max(res, get_score(words[i]) + backtrack(i + 1))
				for c in words[i]:
					letter_count[c] += 1

			return res

		return backtrack(0)