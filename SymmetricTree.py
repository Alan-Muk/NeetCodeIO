class TreeNode:
	def __init__(self, left = None, right = None, val = 0):
		self.left = left
		self.right = right
		self.val = val

class Solution:
	def symmetricTree(self, reet:TreeNode) -> bool:

		def dfs(left, right):
			if not left and not right:
				return True
			if not left or not right:
				return False

			return (left.val == right.val and 
					dfs(left.left, right.right) and 
					dfs(left.right, right.left))

		return dfs(root.left, root.right)