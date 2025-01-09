class Solution:
	def countConsistentString(self, allowed:str, words:list[str]) -> int:
		allowed = set(allowed)
		
		res = len(words)
		for w in words:
			for c in w:
				if c not in allowed:
					res -= 1
					break
		return res