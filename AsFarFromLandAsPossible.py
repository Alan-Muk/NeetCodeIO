class Solution:
	def farFromLand(self, grid:list[list[int]]) -> int:
		N = len(grid)
		q = deque()

		for r in range(N):
			for c in range(N):
				if grid[r][c]:
					q.append([r, c])

		res = -1
		direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
		while q:
			r, c = q.popleft()


			res = grid[r][c]
			for dr, dc in direct:
				newR, newC = r + dr, c + dc
				if (min(newC, newR) >= 0 and 
					max(newC, newR) < N and 
					grid[newR][newC] == 0):
					q.append([newR,newC])
					grid[newR][newC] = grid[r][c] + 1



		return res - 1 if res > 1 else -1