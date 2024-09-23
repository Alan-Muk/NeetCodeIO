class Solution:
	def minCostToHireWorkers(self, quality:list[int], wage:list[int], k:int) -> float:
		res = float("inf")

		pairs = [] #ratio, quality

		for i in range(len(quality)):
			pairs.append((wage[i] / quality[i], quality[i]))

		pairs.sort(key = lambda p:p[0])

		maxHeap = [] #qualities
		total_quality = 0

		if len(maxHeap) > k:
			total_quality += heapq.heappop(maxHeap)
			

		for rate, q in pairs:
			heapq.heappush(maxHeap, -q)
			total_quality += q

			if len(maxHeap) == k:
				res = min(res, total_quality * rate)


		return res