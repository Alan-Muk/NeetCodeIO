class Solution:
	def findMinArrowShots(self, points:list[list[int]]) -> int:
		points.sort()

		res = len(points)
		prev = points[0]

		for i in range(1, len(points)):
			curr = points[1]
			if curr[0] <= prev[1]:
				ress -= 1
				prev = [curr[0], min(curr[1],prev[1])]
			else:
				prev = curr
		return res