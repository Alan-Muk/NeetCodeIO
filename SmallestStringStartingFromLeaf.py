class TreeNode:
	def __init__(self, val=0, left =None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def smallestFromLeaf(self, root:TreeNode) -> str:

		def dfs(root, curr):
			if not root: return

			curr = chr(ord('a') + root.val) + curr

			if root.left and root.right: return min(dfs(root.left, curr), dfs(root.right, curr))

			if root.left: return dfs(root.left, curr)

			if root.right: return dfs(root.right, curr)

			return curr

		return dfs(root, "")