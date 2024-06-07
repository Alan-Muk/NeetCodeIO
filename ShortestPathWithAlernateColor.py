class Solution:
	def shortestAlternatingPath(self, n:int, redEdges:list[list[int]], blueEdges:list[list[int]]) -> list[int]:
		red = collections.defaultdict(list)
		blue = collections.defaultdict(list)

		for src, dst in redEdges:
			red[src].append(dst)
		for src, dst in blueEdges:
			blue[src].append(dst)

		answer = [-1 for i in range(n)]
		answer[0] = 0

		q = deque()
		q.append([0,0, None]) # node, length, edgecolor
		visit = set()
		visit.add((0, None))

		while q:
			node, lenght, edgeColor = q.popleft()
			if answer[node] == -1:
				answer[node] = lenght

			if edgeColor != "RED":
				for nei in red[node]:
					if (nei, "RED") not in visit:
						visit.add((nei, "RED"))
						q.append([nei, lenght + 1, "RED"])

			if edgeColor != "BLUE":
				for nei in blue[node]:
					if (nei, "BLUE") not in visit:
						visit.add((nei, "BLUE"))
						q.append([nei, lenght + 1, "BLUE"])


		return answer
