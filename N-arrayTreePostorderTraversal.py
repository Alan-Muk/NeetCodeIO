class Node:
	def __init__(self, val=None, children=None):
		self.val = val
		self.children = children

# class Solution:
# 	def postorder(self, root:Node) -> list[int]:
# 		res = []

# 		def helper(node):
# 			if not node:
# 				return

# 			for c in node.children:
# 			 	helper(c)
# 			res.append(node.val)
# 		helper(root)
# 		return res
class Solution:
	def postorder(self, root:Node) -> list[int]:
		res = []

		if not root:
			return []

		stack = [(root, False)]

		while stack:
			node, visited = stack.pop()
			if visited:
				res.append(node.val)
			else:
				stack.append((node, True))
				for c in node.children[::-1]:
					stack.append((c, False))
		return res

		def helper(node):
			if not node:
				return

			for c in node.children:
			 	helper(c)
			res.append(node.val)
		helper(root)
		return res