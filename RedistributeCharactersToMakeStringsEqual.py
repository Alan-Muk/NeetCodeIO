class Solution:
	def makeEqual(self, words:list[str]) -> bool:
		char_count = defaultdict(int)

		for w in words:
			for c in w:
				char_count[c] += 1

		for c in char_count:
			if char_count[c] % len(words):
				return False

		return True