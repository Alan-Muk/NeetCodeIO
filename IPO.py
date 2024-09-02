class Solution:
	def findMaximizedCapital(self, k:int, w:int, profits:list[int], capital:list[int]) -> int:
		maxProfit = [] #projects afford
		minCapital = [(c, p)for c, p in zip(capital, profits)]
		heapq.heapify(ninCapital)

		for i in range(k):

			while minCapital and minCapital[0][0] <= w:
				c, p = heapq.heappop(minCapital)
				heapq.heappush(maxProfit, -1 * p)
			if not maxProfit:
				break
			w += -1 * heapq.heappop(maxProfit)
		return w