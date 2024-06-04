class Solution:
	def checkIfPrerequisite(self, numCourses:int, prerequisites:list[list[int]], queries:list[list[int]]) -> list[list[int]]:
		adj = defaultdict(list)
		for prereq, crs in prerequisites:
			adj[crs].append(prereq)

		def dfs(crs):
			if crs not in prereqMap:
				prereqMap[crs] = set()
				for prereq in adj[crs]:
					prereqMap[crs] |= dfs(prereq)
				prereqMap[crs].add(crs)

			return prereqMap[crs]

		prereqMap = {} 
		for crs in range(numCourses):
			dfs(crs)

		res = []
		for u, v in queries:
			res.append(u in prereqMap[v])
		return res