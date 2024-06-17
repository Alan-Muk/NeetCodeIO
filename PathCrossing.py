class Solution:
	def path(self, s:str) -> bool:
		dir = {
				"N":[0, 1],
				"S":[0, -1],
				"W":[-1, 0],
				"E":[1, 0]
				}
		visit = set() #(x,y)
		x, y = 0, 0

		for c in path:
			visit.add((x, y))
			dx, dy = dir[c]
			x, y = x + dx, y + dy
			if (x, y) in visit:
				return True

		return False