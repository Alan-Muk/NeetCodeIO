class TreeNode:
	def __init____(self, left=None, right=None, val=0):
		self.left = left
		self.right = right
		self.val = val

class Solution:
	def deleteNode(self, root:TreeNode, key:int) -> TreeNode:
		if not root:
			return root

		if key > root.val:
			root.right = self.deleteNode(root.right, key)
		elif key < root.val:
			root.left = self.deleteNode(root.left, key)
		else:
			if not root.left:
				return root.right
			elif not root.right:
				return root.left

			#min right
			cur = root.rigt
			while cur.left:
				cur = cur.left
			root.val = cur.val
			root.right = self.deleteNode(root.right, root.val)

		return root