class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

# class Solution:
# 	def evaluateTree(self, root:TreeNode) -> bool:
# 		if not root.left and not root.right:
# 			return root.val == 1

# 		if root.val == 2:
# 			return(self.evaluateTree(root.left) and
# 					self.evaluateTree(root.right))

# 		if root.val == 3:
# 			return(self.evaluateTree(root.left) or
# 					self.evaluateTree(root.right))

class Solution:
	def evaluateTree(self, root:TreeNode) -> bool:
		stack = [root]
		value = {}
		while stack:
			node = stack.pop()
			# leaf node
			if not node.left and not node.right:
				value[node] = node.val == 1
			#non-leaf node
		else:
			#childern visited
			if node.left in value and node.right in value:
				if node.val == 2:
					value[node] = value[node.left] or value[node.right]
				if node.val == 3:
					value[node] = value[node.left] and value[node.right]
			#children not visited
			else:
				stack.extend([node, node.left, node.right])
		return value[root]