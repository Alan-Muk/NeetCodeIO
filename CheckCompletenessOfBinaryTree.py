class TreeNode:
	def __init__(self, left=None, right=None, val=0):
		self.left = left
		self.right = right
		self.val = val


class Solution:
	def treeComplete(self, head:TreeNode) -> bool:
		q = deque([root])

		while q:
			node = q.popleft()

			if node:
				q.append(node.left)
				q.append(node.right)
			else:
				while q:
					if q.popleft():
						return False

		return True