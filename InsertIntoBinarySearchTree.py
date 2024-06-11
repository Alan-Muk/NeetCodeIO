class TreeNode:
	def __init__(self, left=None, right=None, val=0):
		self.left = left
		self.right = right
		self.val = val

class Solution:
	def insertIntoTree(self, root:TreeNode, val:int) -> TreeNode:
		if not root:
			return TreeNode(val)

		if val > root.val:
			root.right = self.insertIntoTree(root.right, val)
		else:
			root.left = self.insertIntoTree(root.left, val)

		return root