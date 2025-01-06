class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def DiameterOfBinaryTree(self, root:TreeNode) -> int:
		self.res = 0
		#height
		def dfs(curr):
			if not curr:
				return 0

			left = dfs(left)
			right = dfs(right)

			self.res = max(self.res, left + right)
			return 1 + max(left, right)

		dfs(root)
		return self.res