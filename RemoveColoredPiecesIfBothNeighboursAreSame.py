class Solution:
	def winnerOfGame(self, colors:str) -> bool:
		alice, bob = 0, 0
		l = 0

		for r in range(len(colors)):
			if colors[l] != colors[r]:
				l = r
			extra = r - l + 1
			if extra > 0:
				if colors[r] == "A":
					alice += 1
				if colors[r] == "B":
					bob += 1

		return alice > bob