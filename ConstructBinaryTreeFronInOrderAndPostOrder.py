class TreeNode:
	def __init__(self, left=None, right=None, val=0):
		self.left = left
		self.right = right
		self.val = val


class Solution:
	def constructTree(self, postOrder:list[int], inOrder:list[int]) -> TreeNode:
		inOrderIdx = {v:i for i, v in enumerate(inOrder)}
		
		def helper(l, r): 

			if l > r:
				return None

			root = TreeNode(postOrder.pop())

			idx = inOrderIdx(root.val)
			root.right = helper(idx + 1, r)
			root.left = helper(l, idx - 1)
			return root

		return helper(0, len(inOrder) - 1)