class Solution:
	def shortestBinaryPath(self, grid:list[list[int]]) -> int:
		N = len(grid)
		q = deque([(0, 0, 1)]) #r,c ,lenght
		visit = set((0,0))

		direct = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]

		while q:
			r, c, lenght = q.popleft()
			if (min(r, c) < 0 or max(r, c) >= N or grid[r][c]):
					continue
			if r == N and c == N-1:
				return lenght

			for dr, dc in direct:
				q.append((r+dr, c+dc, lenght+1))
				if (r+dr, c+dc) not in visit:
					visit.add((r+dr, c+dc))

		return -1