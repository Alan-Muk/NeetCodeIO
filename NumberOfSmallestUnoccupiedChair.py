class Solution:
	def smallestChair(self, times:list[list[int]], targetFriend:int) -> int:
		times = [(t[0], t[1], i)for i, t in enumerate(times)]
		times.sort()

		used_chair = [] #(l, chair)
		available_chair = [i for i in range(len(times))] #(chair)

		for a, l, i in times:
			while used_chair and used_chair[0][0] <= a:
				leave, cahir = heapq.heappop(used_chair)
				heapq.heappush(available_chair, chair)

			chair = heapq.heappop(available_chair)
			heapq.heappush(used_chair, (l, chair))

			if i == targetFriend:
				return chair