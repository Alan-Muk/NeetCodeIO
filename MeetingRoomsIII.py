class Solution:
	def mostBooked(self, n:int, meetings:list[list[int]]) -> int:
		meetings.sort()

		available = [i for i in range(n)]
		used = [] #(endTime, room)
		count = [0] * n #count[n] = meetins

		for start, end in meetings:
			#finish
			while used and start >= used[0][0]:
				_, room = heapq.heappop(used)
				heapq.heappush(available, room)

			# no room is available
			if not available:
				end_time, room = heapq.heappop(used)
				end = end_time +  (end - start)
				heapq.heappush(available, room)

			# room is available
			room = heapq.heappop(available)
			heapq.heappush(used, (end, room))
			count[room] += 1

		return count.index(max(count))