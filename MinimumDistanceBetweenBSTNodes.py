class TreeNode:
	def __init__(self, left=None, right=None, val=0):
		self.left = left
		self.right= right
		self.val =val

class Solution:
	def minimumDistance(self, root:TreeNode) -> int:
		prev, res = None, float("inf")

		def dfs(node):
			if not node:
				return

			dfs(node.left)
			nonlocal prev, res
			if prev:
				res = min(res, node.val - prev.val)
			prev = node
			dfs(node.right)
		dfs(root)
		return res