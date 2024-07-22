class Solution:
	def minimumEffortPath(self, heights:list[list[int]]) -> int:
		ROW, COLS = len(heights), len(heights[0])

		minHeap = [[0, 0, 0]] # [ diff, r, c]
		visit = set()
		directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

		while minHeap:
			diff, r, c = heapq.heappop(minHeap)

			if (r, c) in visit:
				continue
			visit.add((r, c))

			if (r, c) == (ROW-1, COLS-1):
				return diff


			for dr, dc in directions:
				newR, newC = r + dr, c + dc
				if (newR < 0 or newC < 0 or newR == ROW or newC == COLS or (newR, newC) in visit):
					continue

				newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
				heapq.heappush(minHeap, [newDiff, newR, newC])