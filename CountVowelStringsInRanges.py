class Solution:
	def countVowel(self, words:list[str], queries:list[list[int]]) -> list[int]:
		vowel_set = set("aeiou")

		prefix_cnt = [0] * len(words) + 1
		previous = 0
		for i, w in enumerate(words):
			if w[0] in vowel_set and w[-1] in vowel_set:
				previous += 1

			prefix_cnt[i + 1] = previous

		res = [0] * len(queries)

		for i, q in enumerate(queries):
			l, r = q
			res[i] = prefix_cnt[r + 1] - prefix_cnt[l] 

		return res