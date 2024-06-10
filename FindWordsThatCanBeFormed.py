class Solution:
	def FormWords(self, words:list[str], chars:str) -> int:
		count = Counter(chars)
		res = 0

		for w in words:
			cur_word = defaultdict(int)
			good = True
			for c in chars:
				cur_word[c] += 1
				if c not in count or cur_word[c] > count[c]:
					good = False
					break
			if good:
				res += len(w)

		return res