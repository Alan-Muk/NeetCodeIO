class Solution:
	def numTeams(self, ratings:list[int]) -> int:
		res = 0

		for m in range(1, len(ratings) -1):
			left_smaller. right_larger = 0

			for i in range(m):
				if ratings[i] < ratings[m]:
					left_smaller += 1
			for j in range(m+1, len(ratings)):
				if ratings[j] > ratings[m]:
					right_larger += 1

			res += left_smaller * right_larger # ascending

			left_larger = m - left_smaller
			right_smaller = len(ratings) - m - 1 - right_larger
			res += left_larger + right_smaller

		return res