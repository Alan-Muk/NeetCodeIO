class Solution:
	def constrainedSubsetSum(self, nums:list[int], k:int) -> int:
		res = nums[0]
		max_heap = [(-nums[0]), 0]

		for i in range(1, len(nums)):
			while i - max_heap[0][1] > k:
				heapq.heappop(max_heap)

			cur_max = max(nums[i], nums[i] - max_heap[0][0])
			res = max(res, cur_max)
			heapq.heappush(max_heap, (-cur_max, i))

		return res