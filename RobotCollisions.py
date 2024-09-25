class Solution:
	def survivedRobotHealth(self, positions:list[int], health:list[int], directions:str) -> list[int]:
		index_map = { p:i for i, p in enumerate(positions)}
		stack = [] #index

		for p in sorted(positions):
			i = index_map[p]

			if directions[i] == "R":
				stack.append(i)
			else:
				while stack and directions[stack[-1]] == "R" and health[i]:
					j = stack.pop()

					if health[i] > health[j]:
						health[j] = 0
						health[i] -= 1
					elif health[i] < health[j]:
						health[i] = 0
						health[j] -= 1
						stack.append(j)
					else:
						health[i] = health[j] = 0

				if health[i]:
					stack.append(i)

		return [h for h in health if h > 0]