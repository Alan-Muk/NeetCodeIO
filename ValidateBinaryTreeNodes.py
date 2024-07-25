class Solution:
	def validBinaryTree(self, n:int, leftChild:list[int], rightChild:list[int]) -> bool:
		hasParent = set(leftChild + rightChild)
		hasParent.discard(-1)

		if len(hasParent) == n:
			return False

		root = -1
		for i in range(n):
			if i not in hasParent:
				root = i
				break

		visit = set()
		def dfs(i):
			if i == -1:
				return True

			if i in visit:
				return False

			visit.add(i)
			return dfs(leftChild[i]) and dfs(rightChild[i])

		return dfs(root) and len(visit) == n