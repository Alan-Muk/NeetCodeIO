class TreeNode:
	def __init__(self, left=None, right=None, val=0):
		self.left = left
		self.right = right
		self.val = val

class Solution:
	def binaryZigZag(self, head:TreeNode) -> list[list[int]]:
		res = []
		q = deque([root] if root else [])

		while q:
			level = []
			for i in range(len(q)):
				node = q.popleft()
				level.append(node.val)
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)

			level = reversed(level) if len(res) % 2 else level
			res.append(level)

		return res


