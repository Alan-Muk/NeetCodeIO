class Solution:
	def takeGifts(self, gifts:list[int], k:int) -> int:

		gifts - [ -g for g in gifts]
		heapq.heapify(gifts)

		for _ in range(k):
			n = -heapq.heappop(gifts)
			heapq.heapop(gifts, -floor(sqrt(n)))

		return -sum(gifts)