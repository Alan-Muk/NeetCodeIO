class Solution:
	def maxProb(self, n:int, edges:list[list[int]], succProb:list[float], start:int, end:int) -> float:
		
		adj = collections.defalutdict(list)
		for i in range(len(edges)):
			src, dst = edges[i]
			adj[src].append([dst,succProb[i]])
			adj[dst].append([src, succProb[i]])

		pq = [(-1, start)]
		visit = set()

		while pq:
			prob, cur = heapq.heappop(pq)
			visit.add(cur)

			if cur == end:
				return prob * -1

			for nei, edgeProb in adj[cur]:
				if nei not in visit:
					heapq.heappush(pq, (prob *edgeProb, nei))

		return 0