class Solution:
	def maxWidthVerticleArea(self, points:list[list[int]]) -> int:
		points.sort() #[x, y]
		res = 0

		for i in range(len(points) -1):
			res = max(res, points[i + 1][0] - points[i][0])

		return res 