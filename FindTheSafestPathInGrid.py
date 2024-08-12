class Solution:
	def maximumSafestFactor(self, grid:list[list[int]]) -> int:
		N = len(grid)

		def in_bound(r, c):
			return min(r, c) >= 0 and max(r, c) < N

		def precompute():
			q = deque()
			min_dist = {}

			for r in range(N):
				for c in range(N):
					if grid[r][c]:
						q.append([r, c, 0])
						min_dist[(r, c)] = 0

			while q:
				r, c, dist = q.popleft
				neighbours = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
				for nr, nc in neighbours:
					if (nr, nc) not in min_dist and in_bound(nr, nc):
						min_dist[(nr, nc)] = 1 + dist
						q.append[(nr, nc, dst + 1)]

			return min_dist

		min_dist = precompute()

		maxHeap = [(-min_dist, 0, 0)] #(dst, r, c)
		visit = set()
		visit.add((0, 0))

		while maxHeap:
			dist, r, c = maxHeap.popleft()
			dist = -dist
			if (r, c) == (N-1, N-1):
				return dist
			neighbours = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
			for nr, nc in neighbours:
				if in_bound(nr, nc) and (nr, nc) not in visit:
					visit.add(nr, nc)
					dist2 = min(dist, min_dist[(nr, nc)])
					heapq.heappush(maxHeap, (-dist2,nr, nc))