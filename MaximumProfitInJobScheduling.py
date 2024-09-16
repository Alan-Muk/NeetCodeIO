class Solution:
	def jobScheduling(self, startTime:list[int], endTime:list[int], profit:list[int]) -> int:
		intervals = sorted(zip(startTime, endTime, profit))
		cache = {}

		def dfs(i):
			if i == len(intervals):
				return 0
			if i in cache:
				return cache[i]

			#dont include
			res = dfs(i+1)
			#include
			# j = i + 1
			# while j < len(intervals):
			# 	if intervals[i][1] <= intervals[j][0]:
			# 		break
			# 	j += 1
			j = bisect.bisect(intervals,(intervals[i][1], -1, -1))

			res = max(res, intervals[i][2] + dfs(j))
			cache[i] = res
			return res

		return dfs(0)