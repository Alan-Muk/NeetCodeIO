class Solution:
	def informEmployees(self, n:int, headID:int, manager:list[int], informTime:list[int]) -> int:
		adj = collections.defaultdict(list) # manager -> list[employee]

		for i in range(n):
			adj[manager[i]].append(i)

		
		q =deque([(headID, 0)]) # (id, time)
		res = 0

		while q:
			i, time = q.popleft()
			res = max(res, time)

			for emp in adj[i]:
				q.append((emp, time + informTime[i]))

		return res
