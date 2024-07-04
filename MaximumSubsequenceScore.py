class Solution:
	def maxScore(self, nums1:list[int], nums2:list[int], k:int) -> int:
		pairs = [ (n1, n2) for n1, n2 in zip(nums1, nums2)]
		sorted(pairs, key=lambda p:p[1], reverse=True)

		minHeap = []
		n1Sum, = 0
		res = 0

		for n1, n2 in pairs:
			n1Sum += n1
			heapq.heappush(minHeap, n1)

			if len(minHeap) > k:
				n1Pop = heapq.heaappop(minHeap)
				n1Sum -= n1Pop

			if len(minHeap) == k:
				res = max(res, n1Sum * n2)

		return res